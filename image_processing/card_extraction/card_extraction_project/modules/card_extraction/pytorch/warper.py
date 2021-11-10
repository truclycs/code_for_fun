import cv2
import itertools
import numpy as np
from shapely import geometry


class WarpedCard:
    def __init__(self, binary_threshold, contour_area_threshold, vertical_threshold, iou_threshold):
        self.contour_area_threshold = contour_area_threshold
        self.vertical_threshold = vertical_threshold
        self.binary_threshold = binary_threshold
        self.iou_threshold = iou_threshold

    def _order_points(self, points):
        assert len(points) == 4, 'Length of points must be 4'
        left = sorted(points, key=lambda p: p[0])[:2]
        right = sorted(points, key=lambda p: p[0])[2:]
        tl, bl = sorted(left, key=lambda p: p[1])
        tr, br = sorted(right, key=lambda p: p[1])
        return [tl, tr, br, bl]

    def _compute_iou(self, polyA, polyB):
        iou = 0.
        polyA = geometry.Polygon(polyA)
        polyB = geometry.Polygon(polyB)
        if polyA.intersects(polyB):
            iou = polyA.intersection(polyB).area / polyA.union(polyB).area
        return iou

    def _distance(self, point1, point2):
        point1 = np.float64(point1)
        point2 = np.float64(point2)
        return np.linalg.norm(point1 - point2)

    def _intersection_point(self, line1, line2):
        a1 = line1[1][1] - line1[0][1]
        b1 = line1[0][0] - line1[1][0]
        a2 = line2[1][1] - line2[0][1]
        b2 = line2[0][0] - line2[1][0]
        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            return None
        c1 = (a1 / determinant) * line1[0][0] + (b1 / determinant) * line1[0][1]
        c2 = (a2 / determinant) * line2[0][0] + (b2 / determinant) * line2[0][1]
        x = b2 * c1 - b1 * c2
        y = a1 * c2 - a2 * c1
        return [int(x), int(y)]

    def get_convex_hulls(self, mask, binary_threshold, contour_area_threshold, vertical_threshold):
        convex_hulls = []
        binary_image = (mask > binary_threshold).astype(np.uint8)
        binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, np.ones(shape=(5, 5), dtype=np.uint8))
        num_label, label = cv2.connectedComponents(binary_image)
        for i in range(1, num_label):
            contours = cv2.findContours((label == i).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
            contour = contours[0]
            if cv2.contourArea(contour) > contour_area_threshold * mask.size:
                epsilon = 0.004 * cv2.arcLength(contour, closed=True)
                approx_contour = cv2.approxPolyDP(contour, epsilon, closed=True)
                convex_hull = cv2.convexHull(approx_contour)  # approximate contour to reduce number of convex points
                for inc in range(5):
                    if convex_hull.shape[0] <= vertical_threshold:
                        break
                    # approximate convex_hull to reduce number of convex points
                    epsilon = 0.002 * (1 + inc) * cv2.arcLength(contour, closed=True)
                    convex_hull = cv2.approxPolyDP(convex_hull, epsilon, closed=True)

                if 4 <= convex_hull.shape[0] <= vertical_threshold:
                    convex_hulls.append(np.squeeze(np.array(convex_hull), axis=1))

        return convex_hulls

    def get_enclosed_quadrangles(self, mask, binary_threshold, contour_area_threshold, vertical_threshold, iou_threshold):
        quadrangles = []
        boundary = geometry.box(-mask.shape[1], -mask.shape[0], 2 * mask.shape[1], 2 * mask.shape[0])  # boundary of intersection points
        convex_hulls = self.get_convex_hulls(mask, binary_threshold, contour_area_threshold, vertical_threshold)
        for polygon in convex_hulls:
            num_verticals = len(polygon)  # number of verticals must be greater or equal 4
            quadrangle = None
            max_iou = 0
            for (x, y, z, t) in itertools.combinations(range(num_verticals), 4):
                lines = [
                    [polygon[x], polygon[(x + 1) % num_verticals]],
                    [polygon[y], polygon[(y + 1) % num_verticals]],
                    [polygon[z], polygon[(z + 1) % num_verticals]],
                    [polygon[t], polygon[(t + 1) % num_verticals]]
                ]
                points = []
                for i in range(4):
                    point = self._intersection_point(lines[i], lines[(i + 1) % 4])
                    if (not point) or (point in points) or (not boundary.contains(geometry.Point(point))):
                        break
                    points.append(point)

                if len(points) == 4 and geometry.Polygon(self._order_points(points)).is_valid:
                    candidate_quadrangle = self._order_points(points)
                    iou = self._compute_iou(candidate_quadrangle, polygon)
                    if iou > max_iou and iou > iou_threshold:
                        quadrangle = candidate_quadrangle
                        max_iou = iou

            if quadrangle:
                quadrangles.append(quadrangle)

        return quadrangles

    def get_warped_images(self, image, mask_size, quadrangles):
        warped_images = []
        rh, rw = image.shape[0] / mask_size[0], image.shape[1] / mask_size[1]
        warped_locations = np.float32([[[point[0] * rw, point[1] * rh] for point in quad] for quad in quadrangles])

        for quadrangle in warped_locations:
            top_left, top_right, bottom_right, bottom_left = quadrangle

            widthA = self._distance(bottom_right, bottom_left)
            widthB = self._distance(top_right, top_left)
            avgWidth = round((widthA + widthB) / 2)

            heightA = self._distance(top_right, bottom_right)
            heightB = self._distance(top_left, bottom_left)
            avgHeight = round((heightA + heightB) / 2)

            rectangle = np.float32([[0, 0], [avgWidth - 1, 0], [avgWidth - 1, avgHeight - 1], [0, avgHeight - 1]])

            persp_matrix = cv2.getPerspectiveTransform(quadrangle, rectangle)
            warped_image = cv2.warpPerspective(image, persp_matrix, (int(avgWidth), int(avgHeight)))
            warped_images.append(warped_image)

        return warped_images, warped_locations

    def get_warped_scores(self, mask, quadrangles):
        scores = []
        for quadrangle in quadrangles:
            # Prediction confidence
            prediction_score = mask[mask.round().nonzero()].sum() / mask[mask.nonzero()].sum()
            prediction_score = prediction_score.item()

            # Postprocessing confidence
            mask = mask.round()
            card = np.zeros_like(mask, dtype=np.uint8)
            card = cv2.fillPoly(card, np.int32([quadrangle]), (255, 255, 255)) / 255

            inter = card * mask
            union = (card + mask) != 0

            postprocess_score = inter.sum(dtype=np.float32) / union.sum(dtype=np.float32)
            postprocess_score = postprocess_score.item()

            score = prediction_score * postprocess_score
            scores.append(score)

        return scores

    def __call__(self, image, mask):
        quadrangles = self.get_enclosed_quadrangles(mask, self.binary_threshold, self.contour_area_threshold, self.vertical_threshold, self.iou_threshold)
        warped_images, warped_locations = self.get_warped_images(image, mask.shape[:2], quadrangles)
        warped_scores = self.get_warped_scores(mask, quadrangles)

        return warped_images, warped_locations.tolist(), warped_scores
