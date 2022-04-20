import cv2 as cv
import numpy as np
from time import time
from ScreenCapture import WindowCapture


wincap = WindowCapture('WindowName')

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()

    cv.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / time()-loop_time))
    loop_time = time()

    if cv.waitKey(1) == ord('s'):
        VideoRecording.RecordVideo
        break

    #press 'q' with the output window to force exit
    #waits 1ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

window_capture()
print('Done.')