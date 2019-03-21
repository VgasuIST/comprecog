import wx
from utils.Utils import Utils

players = [('Tendulkar', '15000', '100'), ('Dravid', '14000', '1'),
   ('Kumble', '1000', '700'), ('KapilDev', '5000', '400'),
   ('Ganguly', '8000', '50')]


class ComprecogApplication(wx.Frame):
    """
        TODO: Добавить реализацию приложения wxPython
    """

    def __init__(self):
        super(ComprecogApplication, self).__init__(None, title=Utils.PROGRAM_TITLE)
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'name', width=100)
        self.list.InsertColumn(1, 'runs', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(2, 'wkts', wx.LIST_FORMAT_RIGHT, 100)

        for i in players:
            index = self.list.InsertItem(123, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[2])

        box.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(box)
        panel.Fit()
        self.Centre()

        self.Show(True)


