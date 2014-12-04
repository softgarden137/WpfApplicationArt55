import wpf

from System.Windows import Application, Window
from System.Windows import (ResourceDictionary, WindowState,
                            MessageBox, MessageBoxButton, MessageBoxImage, MessageBoxResult)

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplicationArt55.xaml')
        self.Title = "Art55's Animation in IronPython 2.7"
        myResourceDictionary = ResourceDictionary()
        wpf.LoadComponent(myResourceDictionary,'Art55_Resouces.xaml')
        self.Style = myResourceDictionary["CustomWindowChrome"]
        self.Loaded += self.mySetWinButton

    def mySetWinButton(self,sender,e):
        win = sender
        wt = win.Template
        (wt.FindName("Label1",win)).MouseLeftButtonDown += self.OnMove
        (wt.FindName("Label1",win)).MouseDoubleClick += self.OnMaximam
        (wt.FindName("Button1",win)).Click += self.OnMimimam
        (wt.FindName("Button2",win)).Click += self.OnMaximam
        (wt.FindName("Button3",win)).Click += self.OnClose

    def OnClose(self,sender, e):
        window = sender.TemplatedParent
        r = MessageBox.Show(
            "Window close?",
            window.Title,
            MessageBoxButton.YesNo,
            MessageBoxImage.Warning )
        if r == MessageBoxResult.No:
            pass
        else:
            window.Close()

    def OnMove(self,sender, e):
        window = sender.TemplatedParent
        window.DragMove()

    def OnMaximam(self,sender, e):
        window = sender.TemplatedParent
        if (window.WindowState != WindowState.Maximized) :
            window.WindowState = WindowState.Maximized
        else:
            window.WindowState = WindowState.Normal

    def OnMimimam(self,sender, e):
        window = sender.TemplatedParent
        if (window.WindowState != WindowState.Minimized) :
            window.WindowState = WindowState.Minimized
        else:
            window.WindowState = WindowState.Normal

if __name__ == '__main__':
    Application().Run(MyWindow())

