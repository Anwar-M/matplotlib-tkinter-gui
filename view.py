import tkinter as Tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2Tk

from side_panel import SidePanel
# from side_panel_left import SidePanelL

class View():
    x_min = -1
    x_max = 1
    y_min = -1
    y_max = 1
    slider_val1 = 0
    slider_val2 = 200
    
    def __init__(self, master):
        
        self.frame = Tk.Frame(master)
        
        self.slider_value = Tk.StringVar()
        self.slider = Tk.Scale(master, from_=self.slider_val1, to=self.slider_val2, \
                               orient=Tk.HORIZONTAL, length=800, showvalue=0, \
                               variable = self.slider_value)
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
        
    def get_updated_xlim(self):
        xmin = self.x_min
        xmax = self.x_max
        xdel = self.xlim[1] - self.xlim[0]
        slider_delta = self.slider_val2 - self.slider_val1
        
        x_step = ((xmax - xdel) - xmin)/slider_delta
        
        val_now = float(self.slider_value.get())
        
        x_lim = [xmin + x_step*(val_now), (xmin + xdel)  + x_step*(val_now)] # clean-up, 17/08/21
        
        self.sidepanel2.x1_input.delete(0, Tk.END)
        self.sidepanel2.x2_input.delete(0, Tk.END)
        self.sidepanel2.x1_input.insert(0, x_lim[0])
        self.sidepanel2.x2_input.insert(0, x_lim[1])
        
        return x_lim
    
    def axis_update_x(self, event):
        self.xlim = [float(self.sidepanel2.x1_input.get()), float(self.sidepanel2.x2_input.get())]
        
        self.ax0.set_xlim(self.xlim)
        print(self.xlim)
        self.fig.canvas.draw()        
        
    def axis_update_y(self, event):
        self.ylim = [float(self.sidepanel2.y1_input.get()), float(self.sidepanel2.y2_input.get())]
        
        self.ax0.set_ylim(self.ylim)
        print(self.ylim)
        self.fig.canvas.draw()
        
    # def update_after_plot(self, event):
        
    #     self.x_min = min(self.model.res["x"])
    #     self.x_max = max(self.model.res["x"])
    #     self.y_min = min(self.model.res["y"])
    #     self.y_max = max(self.model.res["y"])
        
    #     self.sidepanel2.x1_input.delete(0, Tk.END)
    #     self.sidepanel2.x2_input.delete(0, Tk.END)
    #     self.sidepanel2.y1_input.delete(0, Tk.END)
    #     self.sidepanel2.y2_input.delete(0, Tk.END)
    #     self.sidepanel2.x1_input.insert(0, self.x_min)
    #     self.sidepanel2.x2_input.insert(0, self.x_max)
    #     self.sidepanel2.y1_input.insert(0, self.y_min)
    #     self.sidepanel2.y2_input.insert(0, self.y_max)
        
    #     self.ax0.set_xlim([self.x_min, self.x_max])
    #     self.ax0.set_ylim([self.y_min, self.y_max])