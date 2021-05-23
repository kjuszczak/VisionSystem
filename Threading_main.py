#!/usr/bin/python

import threading
import warnings

from Main import *
from ScreenshotMaker import *


# Create ScreenshotMaker thread class
class ScreenshotMakerThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        # run
        while True:
            place = input("Podaj lokalizację:\n")
            makeScreen(place)
            barrier.wait()
            barrierSecond.wait()

# Create ProcessingMainThread Thread class
class ProcessingMainThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            runMainProcessing(barrier, barrierSecond)


# Create thread lock
threads = []
barrier = threading.Barrier(2)
barrierSecond = threading.Barrier(2)

# Create new threads
screenshotMakerThread = ScreenshotMakerThread(1, "ScreenshotMaker-Thread")
processingMainThread = ProcessingMainThread(2, "ProcessingMain-Thread")

# Start new Threads
screenshotMakerThread.start()
processingMainThread.start()

# Add threads to thread list
threads.append(screenshotMakerThread)
threads.append(processingMainThread)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")