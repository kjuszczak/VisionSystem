# import the necessary packages
from sklearn.svm import LinearSVC
import cv2
import os
import MouseHandler

from Descriptor import Descriptor

DPI = 96


def getCmFromPixels(pixels):
    return (pixels * 2.54) / DPI


def getAreaValueInMeters(counter, pixels):
    cm = getCmFromPixels(pixels)
    realDistance = cm * 200
    return counter * (realDistance * realDistance)


def runMainProcessing(barrier=None, barrierSecond=None):
    # initialize the local descriptor along with
    # the data and label lists
    desc = Descriptor((20, 4))
    data = []
    labels = []

    folder_las = 'training/las'
    folder_nie_las = 'training/nie_las'
    # loop over the training images
    for filename in os.listdir(folder_las):
        # load the image, convert it to grayscale, and describe it
        image = cv2.imread(os.path.join(folder_las, filename))
        if image is not None:
            # label and data lists
            labels.append('las')
            data.append(desc.describe(image))

    for filename in os.listdir(folder_nie_las):
        # load the image, convert it to grayscale, and describe it
        image = cv2.imread(os.path.join(folder_nie_las, filename))
        if image is not None:
            # extract the label from the image path, then update the
            # label and data lists
            labels.append('nie_las')
            data.append(desc.describe(image))

    # train a Linear SVM on the data
    model = LinearSVC(C=250.0, max_iter=2500000)
    model.fit(data, labels)

    while True:
        if barrier is not None:
            barrier.wait()

        img = cv2.imread('processing_image.jpg')
        clone = img.copy()

        pixels = 20

        MouseHandler.img = img
        cv2.namedWindow("img")
        cv2.setMouseCallback("img", MouseHandler.click_and_crop)
        print("Zaznacz teren na mapie!")
        while True:
            # display the image and wait for a keypress
            cv2.imshow("img", img)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("r"):
                img = clone.copy()
                MouseHandler.img = img
            elif key == ord("c"):
                break
            elif len(MouseHandler.refPt) == 2:
                cropped_img = img[MouseHandler.refPt[0][1]:MouseHandler.refPt[1][1],
                                    MouseHandler.refPt[0][0]:MouseHandler.refPt[1][0]]

                MouseHandler.refPt = []

                height, width, channels = cropped_img.shape
                height = int(height / pixels) * pixels
                width = int(width / pixels) * pixels
                print(height, width)
                cropped_img = cropped_img[0:height, 0:width]

                counter = 0

                y = 0
                x = 0
                while y+pixels <= height:
                    while x+pixels <= width:
                        crop_img = cropped_img[y:y+pixels, x:x+pixels]

                        prediction = model.predict(desc.describe(crop_img).reshape(1, -1))

                        if prediction[0] == 'las':
                            h, w, ch = crop_img.shape
                            cv2.rectangle(crop_img, (0, 0), (w-1, h-1), (0, 0, 255), 1)
                            cv2.putText(crop_img, '.', (5, 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            counter = counter + 1

                        x = x + pixels
                    x = 0
                    y = y + pixels

                mSquare = getAreaValueInMeters(counter, pixels)
                print('Las zajmuję: {mSquare:.3f} [m^2], {ar:.3f} [ar], {har:.3f} [hektar], {km:.3f} [km^2]'.format(mSquare=mSquare, ar=mSquare/100, har=mSquare/10000, km=mSquare/1000000))

        cv2.destroyAllWindows()

        if barrierSecond is not None:
            barrierSecond.wait()

# runMainProcessing()
