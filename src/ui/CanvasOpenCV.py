import wx
import cv2 as cv


class CanvasOpenCV(wx.Panel):
    image = None

    def __init__(self, parent):
        super(CanvasOpenCV, self).__init__(parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_size(self, event):
        event.Skip()
        self.Refresh()

    def on_paint(self, event):
        w, h = self.GetClientSize()
        #dc = wx.AutoBufferedPaintDC(self)
        dc = wx.BufferedPaintDC(self)
        dc.Clear()

        if self.image is not None:
            resimg = cv.resize(self.image, (w-4, h-4))
            resimg = cv.cvtColor(resimg, cv.COLOR_RGBA2BGR)
            btm = wx.Bitmap.FromBuffer(w-4, h-4, resimg)
            dc.DrawBitmap(btm, 2, 2)

        dc.SetBrush(wx.Brush(wx.BLACK, wx.TRANSPARENT))

        dc.SetPen(wx.Pen(wx.BLACK, 1))
        dc.DrawRectangle(0, 0, w-1, h-1)

        dc.SetPen(wx.Pen(wx.WHITE, 1))
        dc.DrawRectangle(1, 1, w-3, h-3)

    def set_image(self, image):
        self.image = image
        self.Refresh()
