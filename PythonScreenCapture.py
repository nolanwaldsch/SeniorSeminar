import cv2 as cv
import numpy as np
from time import time
import win32gui, win32ui, win32con


#finds the names of active windows
def list_window_names():
    def winEnumHandler(hwnd,ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)

list_window_names()

def window_capture():
    w = 1920 # set this
    h = 1080 # set this
    bmpfilenamename = "out.bmp" #set this

    #hwnd = win32gui.FindWindow(None, windowname)
    hwnd = None

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt( (0,0), (w, h) , dcObj, (0,0), win32con.SRCCOPY)
    
    #save the screenshot
    #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
    signedintsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype = 'uint8')
    img.shape = (h, w, 4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


    #dropping alpha channel, or cv.matchTemplate()will throw an eror
    img = img [...,:3]
    img = np.ascontiguousarray(img)

    return img

loop_time = time()
while(True):
    screenshot = window_capture()

    cv.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / time()-loop_time))
    loop_time = time()

    #press 'q' with the output window to force exit
    #waits 1ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

window_capture()
print('Done.')