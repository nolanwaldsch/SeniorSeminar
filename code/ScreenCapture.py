import numpy as np
import win32gui, win32ui, win32con

class WindowCapture:

    #initializing width and height
    w = 0
    h = 0
    hwnd = 0
    cropped_x = 0
    cropped_y = 0
    offset_x
    offset_y


    def __init__(self, window_name):

         self.hwnd = win32gui.FindWindow(None, window_name)
         if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))

        #defines monitor width and height
         wimdow_rect = win32gui.GetWindowRect(self.hwnd)
         self.w = window_rect[2] - window_rect[0]
         self.h = window_rect[3] - window_rect[1]

         #account for window border and title bar
         border_pixels = 8
         titlebar_pixels = 30
         self.w = self.w - (border_pixels * 2)
         self.h = self.h - titlebar_pixels - border_pixels
         self.cropped_x = border_pixels
         self.cropped_y = titlebar_pixels 

        #set the croped coords offset so we can translate the screenshot images into actual screen positions
         self.offset_x = window_rect[0] + self.cropped_x
         self.offset_y = window_rect[1] + self.cropped_y
         

    def get_screenshot(self):

        #get window image data
         wDC = win32gui.GetWindowDC(self.hwnd)
         dcObj = win32ui.CreateDCFromHandle(wDC)
         cDC = dcObj.CreateCompatibleDC()
         dataBitMap = win32ui.CreateBitmap()
         dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
         cDC.SelectObject(dataBitMap)
         cDC.BitBlt( (0,0), (self.w, self.h) , dcObj, (cropped_x, cropped_y), win32con.SRCCOPY)
        
         #save the screenshot
         #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
         signedintsArray = dataBitMap.GetBitmapBits(True)
         mg = np.fromstring(signedIntsArray, dtype = 'uint8')
         img.shape = (self.h, self.w, 4)

         # Free Resources
         dcObj.DeleteDC()
         cDC.DeleteDC()
         win32gui.ReleaseDC(hwnd, wDC)
         win32gui.DeleteObject(dataBitMap.GetHandle())


         #dropping alpha channel, or cv.matchTemplate()will throw an eror
         img = img [...,:3]
         img = np.ascontiguousarray(img)

         return img
    
    #grabs name of every window that is open
    def list_window_names(self):
         def winEnumHandler(hwnd,ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)

    '''
    translate a pixel position on a screen shot image  to a pixel on the screen.
    pos = (x, y)
    WARNING: if you move the window being captured after execution has started, this will
    return incorrect coordinates'''
    def get_screen_position(self, pos):
         return (pos[0] + self.offset_x, pos[1] + self.offset_y)