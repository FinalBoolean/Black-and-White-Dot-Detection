from lib2to3.pgen2 import grammar
import cv2
path = "white.png"

# reading the image in a grayscale mode
gray = cv2.imread(path, 0)
blurred = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)

# threshold
th, threshed = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# findcontours
cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
#print(cnts)

# filter by area
s1 = 3
s2 = 20
xcnts = []

for cnt in cnts:
    if s1 < cv2.contourArea(cnt) and cv2.contourArea(cnt) < s2:
        xcnts.append(cnt)

# printing output
print("\nDots number: {}".format(len(xcnts)))