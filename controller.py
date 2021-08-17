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
        
        self.view.sidepanel2.x1_input.bind("<KeyRelease>", self.view.axis_update_x)
        self.view.sidepanel2.x2_input.bind("<KeyRelease>", self.view.axis_update_x)
        self.view.sidepanel2.y1_input.bind("<KeyRelease>", self.view.axis_update_y)
        self.view.sidepanel2.y2_input.bind("<KeyRelease>", self.view.axis_update_y)
 
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
        x_lim = self.view.get_updated_xlim()
        self.view.ax0.set_xlim(x_lim)
        self.view.fig.canvas.draw()
 
    def my_plot(self, event):
        self.model.calculate()
        # self.view.ax0.clear()
        self.view.ax0.plot(self.model.res["x"], self.model.res["y"],  'go-', linewidth=2, markersize=4)
        # self.view.update_after_plot
        
        self.view.x_min = min(self.model.res["x"])
        self.view.x_max = max(self.model.res["x"])
        self.view.y_min = min(self.model.res["y"])
        self.view.y_max = max(self.model.res["y"])
        
        self.view.sidepanel2.x1_input.delete(0, Tk.END)
        self.view.sidepanel2.x2_input.delete(0, Tk.END)
        self.view.sidepanel2.y1_input.delete(0, Tk.END)
        self.view.sidepanel2.y2_input.delete(0, Tk.END)
        self.view.sidepanel2.x1_input.insert(0, self.view.x_min)
        self.view.sidepanel2.x2_input.insert(0, self.view.x_max)
        self.view.sidepanel2.y1_input.insert(0, self.view.y_min)
        self.view.sidepanel2.y2_input.insert(0, self.view.y_max)
        
        self.view.ax0.set_xlim([self.view.x_min, self.view.x_max])
        self.view.ax0.set_ylim([self.view.y_min, self.view.y_max])
        self.view.fig.canvas.draw()