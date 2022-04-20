import cv2
import numpy as np
from time import time
from ScreenCapture import WindowCapture


wincap = WindowCapture('WindowName')

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()

    cv2.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / time()-loop_time))
    loop_time = time()


   # if cv2.waitKey(1) == ord('s'):
     #   VideoRecording.RecordVideo
     #   VoiceRecording.AudioRecording
     #   break
    #press 'q' with the output window to force exit
    #waits 1ms every loop to process key presses
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

window_capture()
print('Done.')