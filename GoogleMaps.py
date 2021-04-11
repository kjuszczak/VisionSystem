from io import BytesIO
import requests
import cv2

URL = "http://maps.googleapis.com/maps/api/staticmap?center=-30.027489,-51.229248&size=800x800&zoom=14&sensor=false"

response = requests.get(URL)

test = response.content

buffer = 2

# with open('hyderabad.png', 'wb') as file:
#    # writing data into the file
#    file.write(response.content)
#
# image = cv2.imread('hyderabad.png')
# cv2.imshow("Image", image)
# cv2.waitKey(0)