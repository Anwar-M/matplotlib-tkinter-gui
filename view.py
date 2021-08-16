import tkinter as Tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2Tk

from side_panel import SidePanel
# from side_panel_left import SidePanelL

class View():
    def __init__(self, master):
        
        self.frame = Tk.Frame(master)
        
        # self.bottompanel = Tk.Frame(master, bg="green", height = 10, width = 100)
        # self.bottompanel.pack(side=Tk.BOTTOM, fill=None, expand=0)
        self.slider_value = Tk.StringVar()
        self.slider = Tk.Scale(master, from_=0, to=200, orient=Tk.HORIZONTAL, length=800, showvalue=0, variable = self.slider_value)
        self.slider.set(100)
        self.slider.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=0)
        
        self.sidepanel = SidePanel(master, 'left')
        
        
        self.fig = Figure(figsize=(8, 4.5), dpi=80)
        self.ax0 = self.fig.add_axes(
            (0.1, .1, .80, .80), frameon=True)
        # self.ax0 = self.fig.add_subplot(111)
        self.ax0.autoscale(False)
        self.ax0.grid(True)
        self.frame.pack(side=Tk.LEFT, fill=None, expand=0)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.draw()
        
        self.sidepanel2 = SidePanel(master, 'right')
        
        
        # self.toolbar = NavigationToolbar2Tk(self.canvas, master)
        # self.toolbar.update()
        # self.canvas.get_tk_widget().pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)