# import the necessary packages
from LocalBinaryPatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2
import os

# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns(24, 8)
data = []
labels = []

folder_las = 'training/las'
folder_nie_las = 'training/nie_las'
# loop over the training images
for filename in os.listdir(folder_las):
    # load the image, convert it to grayscale, and describe it
    image = cv2.imread(os.path.join(folder_las, filename))
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = desc.describe(gray)
        # extract the label from the image path, then update the
        # label and data lists
        labels.append('las')
        data.append(hist)

for filename in os.listdir(folder_nie_las):
    # load the image, convert it to grayscale, and describe it
    image = cv2.imread(os.path.join(folder_nie_las, filename))
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = desc.describe(gray)
        # extract the label from the image path, then update the
        # label and data lists
        labels.append('nie_las')
        data.append(hist)

# train a Linear SVM on the data
model = LinearSVC(C=100.0, random_state=42)
model.fit(data, labels)

folder = 'testing'
# loop over the testing images
for filename in os.listdir(folder):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(os.path.join(folder, filename))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))

    # display the image and the prediction
    cv2.putText(image, prediction[0], (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    cv2.waitKey(0)