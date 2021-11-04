import cv2
import pytesseract

img = cv2.imread('textlines/0001_0.png')
print(pytesseract.image_to_string(img))
