import cv2
img = cv2.imread("training/nie_las/1.png")
height, width, channels = img.shape
y=0
x=0
h=int(height/4)
w=int(width/4)
# cv2.imshow("Image", img)
while y+h < height:
    while x+w < width:
        crop_img = img[y:y+h, x:x+w]
        cv2.imshow("cropped", crop_img)
        cv2.waitKey(0)
        x = x + w
    x = 0
    y = y + h