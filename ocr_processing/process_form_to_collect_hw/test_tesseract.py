import cv2
import pytesseract
from pytesseract import Output


img = cv2.imread('textlines/0001_0.png')
s = pytesseract.image_to_string(img, config=Output.DICT)
print(s[:4])
