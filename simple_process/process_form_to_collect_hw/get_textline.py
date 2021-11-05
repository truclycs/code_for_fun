import cv2
import pytesseract
import numpy as np
import itertools
from pathlib import Path
from shapely.geometry import box, Point, Polygon

MIN_AREA = 5000
MAX_AREA = 500000

CROP_PIXELS = 5
PADDING = 5
DISTANCE = 0.1
# RATIO_HEIGHT = 0.3
# RATIO_WIDTH = 1

TEXTLINES_DIR = '/home/trucly/Documents/DATASET/hw_collect/textlines/'
IMGAES_DIR = '/home/trucly/Documents/DATASET/hw_collect/images/'
TEXT_FILES_DIR = '/home/trucly/Documents/DATASET/hw_collect/text_files/'


def get_data(data_path):
    with open(data_path, "r") as f:
        data = f.read()
    return data.split('\n')


def save_file(file_path, data):
    data.sort()
    with open(file_path, 'w') as f:
        for label in data:
            f.write(label)


def distance(point1, point2):
    point1 = np.float64(point1)
    point2 = np.float64(point2)
    return np.linalg.norm(point1 - point2)


def distance2(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def get_warped_image(image, quadrangle):
    top_left, top_right, bottom_right, bottom_left = quadrangle

    widthA = distance(bottom_right, bottom_left)
    widthB = distance(top_right, top_left)
    avgWidth = round((widthA + widthB) / 2)

    heightA = distance(top_right, bottom_right)
    heightB = distance(top_left, bottom_left)
    avgHeight = round((heightA + heightB) / 2)

    rectangle = np.float32([[0, 0], [avgWidth - 1, 0], [avgWidth - 1, avgHeight - 1], [0, avgHeight - 1]])

    persp_matrix = cv2.getPerspectiveTransform(quadrangle, rectangle)
    warped_image = cv2.warpPerspective(image, persp_matrix, (int(avgWidth), int(avgHeight)))

    return warped_image


class EnclosingQuadrilateral:
    def __init__(self):
        self.binary_threshold = 0.6
        self.area_threshold = 0.0
        self.vertical_threshold = 20
        self.iou_threshold = 0.8

    def _order_points(self, points):
        assert len(points) == 4, 'Length of points must be 4'
        left = sorted(points, key=lambda p: p[0])[:2]
        right = sorted(points, key=lambda p: p[0])[2:]
        tl, bl = sorted(left, key=lambda p: p[1])
        tr, br = sorted(right, key=lambda p: p[1])
        return [tl, tr, br, bl]

    def _compute_iou(self, polyA, polyB):
        iou = 0.
        polyA = Polygon(polyA)
        polyB = Polygon(polyB)
        if polyA.intersects(polyB):
            iou = polyA.intersection(polyB).area / polyA.union(polyB).area
        return iou

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

    def _convex_hulls(self, pred, binary_threshold=0.6, area_threshold=0.0, vertical_threshold=20):
        convex_hulls = []
        binary_image = (pred > binary_threshold).astype(np.uint8)
        binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, np.ones(shape=(5, 5), dtype=np.uint8))
        num_label, label = cv2.connectedComponents(binary_image)
        for i in range(1, num_label):
            contours, _ = cv2.findContours((label == i).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contour = contours[0]
            if cv2.contourArea(contour) > area_threshold * pred.size:
                epsilon = 0.009 * cv2.arcLength(contour, closed=True)
                approx_contour = cv2.approxPolyDP(contour, epsilon, closed=True)
                convex_hull = cv2.convexHull(approx_contour)  # approximate contour to reduce num of points
                for inc in range(5):
                    if convex_hull.shape[0] <= vertical_threshold:
                        break
                    epsilon = 0.002 * (1 + inc) * cv2.arcLength(contour, closed=True)
                    convex_hull = cv2.approxPolyDP(convex_hull, epsilon, closed=True)

                if 4 <= convex_hull.shape[0] <= vertical_threshold:
                    convex_hulls.append(np.squeeze(np.array(convex_hull), axis=1))

        return convex_hulls

    def _enclosing_quadrilateral(self, pred, convex_hulls, iou_threshold):
        enclosing_quads = []
        x1, x2 = [-pred.shape[0], 2 * pred.shape[0]]
        y1, y2 = [-pred.shape[1], 2 * pred.shape[1]]
        boundary = box(x1, y1, x2, y2)
        for polygon in convex_hulls:
            num_verticals = len(polygon)
            max_iou = 0.
            enclosing_quad = None
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
                    if (not point) or (point in points) or (not boundary.contains(Point(point))):
                        break
                    points.append(point)

                if len(points) == 4 and Polygon(self._order_points(points)).is_valid:
                    poly = Polygon(points)
                    if MIN_AREA < poly.area < MAX_AREA:
                        candidate_quad = self._order_points(points)
                        iou = self._compute_iou(candidate_quad, polygon)
                        if iou > max_iou and iou > iou_threshold:
                            enclosing_quad = candidate_quad
                            max_iou = iou

            if enclosing_quad:
                enclosing_quads.append(enclosing_quad)

        return enclosing_quads

    def __call__(self, pred):
        convex_hulls = self._convex_hulls(pred, self.binary_threshold, self.area_threshold, self.vertical_threshold)
        enclosing_quads = self._enclosing_quadrilateral(pred, convex_hulls, self.iou_threshold)
        return enclosing_quads


def crop_image(image):
    image_copy = image.copy()
    height, width, _ = image.shape
    height, width = height - CROP_PIXELS, width - CROP_PIXELS
    image = image[CROP_PIXELS: height, CROP_PIXELS: width]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (5, 5), 0)
    # ret, thresh1 = cv2.threshold(gray, 135, 255, cv2.THRESH_BINARY_INV)
    thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    rects = []
    for contour in contours:
        rects.append(cv2.boundingRect(contour))
    rects.sort(key=lambda x: x[0])

    y_top, y_bottom = height, 0
    x_left, x_right = width, 0
    for rect in rects:
        x, y, w, h = rect
        # if h >= height * RATIO_HEIGHT and w <= width * RATIO_WIDTH and (x - x_right) < DISTANCE * width:
        if x - x_right < DISTANCE * width:
            y_top = min(y_top, y)
            y_bottom = max(y_bottom, y + h)
            x_left = min(x_left, x)
            x_right = max(x_right, x + w)

    crop_image = image_copy[max(0, y_top - PADDING): min(y_bottom + PADDING, height),
                            max(0, x_left - PADDING): min(x_right + PADDING, width)]

    return crop_image


if __name__ == '__main__':
    patterns = ['*.jpg', '*.png']
    paths = []
    for pattern in patterns:
        paths += list(Path(IMGAES_DIR).glob(f'**/{pattern}'))

    all_label = []
    for path in paths:
        image = cv2.imread(str(path))
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        minEnclosingQuad = EnclosingQuadrilateral()
        enclosing_quads = minEnclosingQuad(binary_image)

        idx = None
        text = []
        imagename_file = []
        for i, polygon in enumerate(enclosing_quads):
            quadrangle = np.float32(polygon)
            warp_image = get_warped_image(image, quadrangle)

            if i == 0:
                idx = str(pytesseract.image_to_string(warp_image)[:4])
                text = get_data(TEXT_FILES_DIR + idx + '.txt')
                print(idx)
                continue

            filename = idx + '_' + str(i)

            cv2.imwrite(TEXTLINES_DIR + filename + '_uncrop.png', warp_image)

            warp_image = crop_image(warp_image)
            cv2.imwrite(TEXTLINES_DIR + filename + '.png', warp_image)

            with open(TEXTLINES_DIR + filename + '.txt', 'w') as f:
                f. write(text[i - 1])

            all_label.append(filename + '.png' + '\t' + text[i - 1] + '\n')
            imagename_file.append(filename + '.png')
        #     for i, point in enumerate(polygon):
        #         cv2.circle(image, center=tuple(point), radius=3, color=(0, 0, 255), thickness=-1)
        #         cv2.line(image, pt1=tuple(polygon[i % len(polygon)]),
        #                  pt2=tuple(polygon[(i + 1) % len(polygon)]), color=(0, 255, 0), thickness=1)

        # cv2.imwrite('/home/trucly/Documents/DATASET/hw_collect/image_draw/' + str(idx) + '.png', image)

    save_file(TEXTLINES_DIR + 'all_label.txt', all_label)
    save_file(TEXTLINES_DIR + 'imagename_file.txt', imagename_file)
