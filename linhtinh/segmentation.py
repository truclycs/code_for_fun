import cv2
import numpy as np

visualization = False
img_path = "0E59FA70-CA5F-4B80-8673-B8260384CF1F.jpg"
img_paths = [
    "0E59FA70-CA5F-4B80-8673-B8260384CF1F.jpg",
    "3BB3E3CC-D6D3-4D6D-A33E-DCF03BF02DC7.jpg",
    "57ABF66A-5EE5-4B29-B812-B61F0FE1ED32.jpg",
    "317CECEB-3F82-43F9-858E-F5DC6BBAECBA.jpg",
    "A0F74E97-698B-472B-BAEE-E61D5EC6D18C.jpg",
    "BAAEA76C-5C74-4FD3-8A5D-2CE6A50913DC.jpg",
    "C0685E55-6F9D-42A0-A7E6-ABA079550498.jpg",
    "F7E44E69-4630-45A6-8C7D-DBF5BEFCB7D9.jpg"
]

def enhance_image(img):
    #-----Converting image to LAB Color model----------------------------------- 
    lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    #-----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)

    #-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)

    #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl,a,b))

    #-----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    return final

for img_path in img_paths:
    img = cv2.imread(img_path)

    img = enhance_image(img)
    height, width, channels = img.shape
    
    ratio = height / width
    NW = int(500)
    NH = int(NW * ratio)
    # Resize image, convert to gray scale, apply GaussianBlur
    img = cv2.resize(img, (NW, NH), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
    draw_img = img.copy()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (3, 3), 0)

    # Morphology: Blackhat
    blackhat_img = cv2.morphologyEx(gray_img, cv2.MORPH_BLACKHAT, (7, 7))

    # Sobel X
    gradX_img = cv2.Sobel(blackhat_img, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradX_img = np.absolute(gradX_img)
    (minVal, maxVal) = (np.min(gradX_img), np.max(gradX_img))
    gradX_img = (255 * ((gradX_img - minVal) / (maxVal - minVal))).astype("uint8")

    if visualization:
        cv2.imshow('show grad', gradX_img)
        cv2.waitKey()

    # Morphology: Closing
    CLOSE_RECTKERNEL = cv2.getStructuringElement(cv2.MORPH_RECT, (35, 1)) 
    closing_img = cv2.morphologyEx(gradX_img, cv2.MORPH_CLOSE, CLOSE_RECTKERNEL)

    if visualization:
        cv2.imshow('show closing', closing_img)
        cv2.waitKey()

    # Binarize image with OTSU
    thresh = cv2.threshold(closing_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    if visualization:
        cv2.imshow('show otsu', thresh)
        cv2.waitKey()

    OPEN_RECTKERNEL = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 1)) 
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, OPEN_RECTKERNEL)

    if visualization:
        cv2.imshow('show closing 02', thresh)
        cv2.waitKey()

    # Post processing to remove unexpected areas
    thresh = cv2.erode(thresh, None, iterations=2)
    DILATE_RECTKERNEL = cv2.getStructuringElement(cv2.MORPH_RECT, (55, 3))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, DILATE_RECTKERNEL)
    DILATE_RECTKERNEL = cv2.getStructuringElement(cv2.MORPH_RECT, (55, 3))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, DILATE_RECTKERNEL)
    # thresh = cv2.erode(thresh, None, iterations=1)
    # DILATE_RECTKERNEL = cv2.getStructuringElement(cv2.MORPH_RECT, (55, 1))
    # thresh = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, DILATE_RECTKERNEL)

    if visualization:
        cv2.imshow('show final', thresh)
        cv2.waitKey()

    # thresh = cv2.resize(thresh, (width, height), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)

    cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    bouding_boxes = []
    i = 0
    for temp in cnts:
        # if len(cnts) > 25:
        area = cv2.contourArea(temp)
        if area > 500.0:
            (x, y, w, h) = cv2.boundingRect(temp)
            bouding_boxes.append((x, y, w, h))
            i += 1
    if i != 25:
        print("Failed")
        print(i)
        # cv2.imshow('show img', thresh)
        # cv2.waitKey()
    else:
        print("Successful")            

    h_mean = round(sum([bb[3] for bb in bouding_boxes])/len(bouding_boxes))
    sorted(bouding_boxes, key=lambda x: x[1])
    for idx, bb in enumerate(bouding_boxes):
        (x, y, w, h) = bb
        standard_h = max(h_mean, h)
        scale_x = max(0, int(x-w*0.05))
        scale_w = int(w*1.1)
        scale_y = max(0, int(y-standard_h*0.35))
        scale_h = int(standard_h*1.8)
        color = (255, 0, 0) 
            
        start_point = (scale_x, scale_y)
        end_point = (scale_x+scale_w, scale_y+scale_h)
        
        thickness = 1
        draw_img = cv2.rectangle(draw_img, start_point, end_point, color, thickness)
    cv2.imwrite("W_drawed_" + img_path, draw_img)
