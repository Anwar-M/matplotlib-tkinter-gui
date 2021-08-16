import tkinter as Tk

from model import Model
from view import View

from center_window import center_window


class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        center_window(self.root, 1000, 400) # fix the window size
        self.root.resizable(0, 0) # disable resizing
        self.root.iconbitmap("matto.ico")
        self.model = Model()
        self.view = View(self.root)
        self.view.sidepanel.plotBut.bind("<Button>", self.my_plot)
        self.view.sidepanel.clearButton.bind("<Button>", self.clear)
        self.view.slider.bind("<B1-Motion>", self.pan_x)
 
    def run(self):
        self.root.title("Matplotlib GUI")
        self.root.deiconify()
        self.root.mainloop()
 
    def clear(self, event):
        ln = self.view.ax0.get_lines()
        if ln:
            ln.pop(0).remove()
            
        self.view.fig.canvas.draw()
 
    def pan_x(self, event):
        val1 = 1
        val2 = 200
        xmin = -6.3
        xmax = 6.3
        xdel = 2
        
        x_step = ((xmax - xdel) - xmin)/(200)
        
        val_now = float(self.view.slider_value.get())
        
        x_lim = [xmin + x_step*(val_now), (xmin + xdel)  + x_step*(val_now)] # clean-up, 17/08/21
        
        self.view.ax0.set_xlim(x_lim)
        self.view.fig.canvas.draw()  
 
    def my_plot(self, event):
        self.model.calculate()
        # self.view.ax0.clear()
        self.view.ax0.plot(self.model.res["x"], self.model.res["y"],  'go-', linewidth=2, markersize=4)
        self.view.ax0.set_ylim([min(self.model.res["y"]), max(self.model.res["y"])])
        self.view.fig.canvas.draw()