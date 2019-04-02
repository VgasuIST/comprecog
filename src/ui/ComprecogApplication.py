import wx
import os
import numpy
import cv2 as cv

from utils.Utils import Utils
from utils.Visualizer import Visualizer
from utils.ObjectNameTable import ObjectNameTable
from ui.CanvasOpenCV import CanvasOpenCV

from recognition.ContourImageRecognizer import ContourImageRecognizer


class ComprecogApplication:
    app: wx.App

    name_table: ObjectNameTable
    visualizer: Visualizer
    detections: list
    original_image = None
    visualized_image = None

    frame: wx.Frame
    panel: wx.Panel
    canvas: CanvasOpenCV

    image_path_tc: wx.TextCtrl
    rcg_method_cb: wx.ComboBox
    con_list: wx.ListCtrl

    def __init__(self):
        self.app = wx.App()
        self.name_table = ObjectNameTable('resources/localized_names.txt')
        self.visualizer = Visualizer(self.name_table)
        self.frame = wx.Frame(None, -1, Utils.PROGRAM_TITLE)
        self.frame.SetSize(1024, 600)
        self.frame.SetMinSize((800, 600))
        self.panel = wx.Panel(self.frame)
        self.canvas = CanvasOpenCV(self.panel)

        self.fill()

    def load_image(self, path):
        error = 'Невозможно прочитать изображение {}: {}'
        try:
            with open(path, 'rb') as stream:
                bt = bytearray(stream.read())
                arr = numpy.asarray(bt, dtype=numpy.uint8)
                self.original_image = self.visualized_image = cv.imdecode(arr, cv.IMREAD_UNCHANGED)
                error.format(path, 'неизвестная ошибка')
        except EnvironmentError as e:
            error.format(path, e.strerror)

        if self.original_image is None:
            dialog = wx.MessageDialog(self.frame, error, caption='Caption', style=wx.OK | wx.CENTRE)
            dialog.ShowModal()

    def browse_button_click(self, event):
        dialog = wx.FileDialog(
            self.frame,
            'Открыть',
            os.getcwd(),
            '',
            'Изображения (*.jpg;*.jpeg;*.png)|*.jpeg;*.jpg;*.png',
            wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW
        )

        ret = dialog.ShowModal()
        if ret == wx.ID_OK:
            path = dialog.GetPath()
            self.image_path_tc.SetValue(path)
            self.load_image(path)
            self.canvas.set_image(self.visualized_image)
            dialog.Destroy()

    def detect_button_click(self, event):
        self.visualized_image = self.original_image

        rcg_sel = self.rcg_method_cb.GetSelection()
        recognizer = None
        if rcg_sel == 0:
            recognizer = ContourImageRecognizer()

        if recognizer is not None:
            self.detections = recognizer.process_image(self.original_image)
            self.visualized_image = self.visualizer.visualize_detections(self.original_image, self.detections)

        self.canvas.set_image(self.visualized_image)

    def fill(self):
        v_box = wx.BoxSizer(wx.VERTICAL)
        h_box = wx.BoxSizer(wx.HORIZONTAL)

        sizer = wx.GridBagSizer(4, 4)

        control_panel = wx.Panel(self.panel)

        label = wx.StaticText(control_panel, label='Изображение')
        self.image_path_tc = wx.TextCtrl(control_panel)
        self.image_path_tc.SetEditable(False)
        self.image_path_tc.SetMinSize((150, 15))
        button = wx.Button(control_panel, label='Выбор...')
        button.Bind(wx.EVT_BUTTON, self.browse_button_click)
        sizer.Add(label, pos=(0, 0), flag=wx.EXPAND)
        sizer.Add(self.image_path_tc, pos=(0, 1), flag=wx.EXPAND)
        sizer.Add(button, pos=(0, 2), flag=wx.ALIGN_RIGHT)

        label = wx.StaticText(control_panel, label='Способ обнаружения')

        rcg_methods = ["Контурный", "Нейросети"]
        self.rcg_method_cb = wx.ComboBox(control_panel, value=rcg_methods[0], choices=rcg_methods, style=wx.CB_READONLY)
        sizer.Add(label, pos=(1, 0), flag=wx.EXPAND)
        sizer.Add(self.rcg_method_cb, pos=(1, 1), span=(1, 2), flag=wx.BOTTOM | wx.EXPAND)

        button = wx.Button(control_panel, label='Обнаружить')
        button.Bind(wx.EVT_BUTTON, self.detect_button_click)
        sizer.Add(button, pos=(2, 0), span=(1, 3), flag=wx.BOTTOM | wx.EXPAND)

        m_size = control_panel.GetMaxSize()
        control_panel.SetMaxSize((400, m_size[1]))

        sizer.AddGrowableCol(0)
        control_panel.SetSizer(sizer)

        h_box.Add(self.canvas, wx.ID_ANY, flag=wx.EXPAND)
        h_box.Add(control_panel, wx.ID_ANY, flag=wx.EXPAND|wx.ALL, border=10)

        v_box.Add(h_box, wx.ID_ANY, flag=wx.EXPAND)

        self.con_list = wx.ListCtrl(self.panel, style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_VRULES)
        self.con_list.InsertColumn(0, 'Композиция', format=wx.LIST_FORMAT_LEFT, width=500)
        self.con_list.InsertColumn(1, 'Совпадение, %', format=wx.LIST_FORMAT_CENTER, width=100)
        self.con_list.SetMaxSize((self.con_list.GetMaxSize()[0], 200))

        v_box.Add(self.con_list, wx.ID_ANY, flag=wx.EXPAND)

        for i in range(50):
            index = self.con_list.InsertItem(i, 'Test')
            self.con_list.SetItem(index, 1, '100')

        self.panel.SetSizer(v_box)
        pass

    def start(self):
        self.frame.Centre()
        self.frame.Show()
        self.app.MainLoop()
