import tkinter as Tk
import re

class SidePanel():
    FONT_TYPE = "Helvetica 12 bold"
    
    def __init__(self, root, position):
        # self.frame2.grid()
        
        if position == 'left':
            self.frame2 = Tk.Frame(root, bg="gray", width = 100)
            self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=0)
            self.arrange_left()
        elif position == 'right':
            self.frame3 = Tk.Frame(root, width = 100)
            self.frame3.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
            self.arrange_right_labels()
            self.frame4 = Tk.Frame(root, width = 100)
            self.frame4.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
            self.arrange_right_inputs()
        else:
            print('error')
        
        
    def arrange_left(self):
        self.loadBut = Tk.Button(self.frame2, text="Load", height = 1, width = 10)
        self.loadBut.pack(side="top", fill=None, padx=10, pady=5)
        self.plotBut = Tk.Button(self.frame2, text="Plot", height = 1, width = 10)
        self.plotBut.pack(side="top", fill=None, padx=10, pady=5)
        self.clearButton = Tk.Button(self.frame2, text="Clear", height = 1, width = 10)
        self.clearButton.pack(side="top", fill=None, padx=10, pady=5)
        self.saveBut = Tk.Button(self.frame2, text="Save", height = 1, width = 10)
        self.saveBut.pack(side="top", fill=None, padx=10, pady=5)
        self.exitBut = Tk.Button(self.frame2, text="Exit", height = 1, width = 10)
        self.exitBut.pack(side="top", fill=None, padx=10, pady=5)
        
    def arrange_right_labels(self):
        # label_mass_ref = Label(frame)
        # label_mass_ref.grid(column=0, row=0)
        # label_mass_ref.config(text="Tot. [g]")
        self.x1_label = Tk.Label(self.frame3, text="x min: ", height = 1, width = 10, font = self.FONT_TYPE)
        self.x1_label.pack(side="top", fill=None, padx=10, pady=5)
        self.x2_label = Tk.Label(self.frame3, text="x max: ", height = 1, width = 10, font = self.FONT_TYPE)
        self.x2_label.pack(side="top", fill=None, padx=10, pady=5)
        self.y1_label = Tk.Label(self.frame3, text="y min: ", height = 1, width = 10, font = self.FONT_TYPE)
        self.y1_label.pack(side="top", fill=None, padx=10, pady=5)
        self.y2_label = Tk.Label(self.frame3, text="y max: ", height = 1, width = 10, font = self.FONT_TYPE)
        self.y2_label.pack(side="top", fill=None, padx=10, pady=5)
        self.line_label = Tk.Label(self.frame3, text="Markers: ", height = 1, width = 10, font = self.FONT_TYPE)
        self.line_label.pack(side="top", fill=None, padx=10, pady=5)
        self.marker_label = Tk.Label(self.frame3, text="Lines: ", height = 1, width = 10, font = self.FONT_TYPE)
        self.marker_label.pack(side="top", fill=None, padx=10, pady=5)
        
        # self.plotBut = Tk.Button(self.frame3, text="Plot ", height = 1, width = 10)
        # self.plotBut.pack(side="top", fill=None, padx=10, pady=5)
        # self.clearButton = Tk.Button(self.frame3, text="Clear", height = 1, width = 10)
        # self.clearButton.pack(side="top", fill=None, padx=10, pady=5)
        # self.dumButton = Tk.Button(self.frame3, text="Clear", height = 1, width = 10)
        # self.dumButton.pack(side="top", fill=None, padx=10, pady=5)
        
    def arrange_right_inputs(self):
        # def only_numbers(char):
        #     return char.isdigit()
        # def only_numbers(P):
        #     if str.isdigit(P) or P == "":
        #         return True
        #     else:
        #         return False
            
        def validate(string):
            regex = re.compile(r"(\+|\-)?[0-9.]*$")
            result = regex.match(string)
            return (string == ""
                    or (string.count('+') <= 1
                        and string.count('-') <= 1
                        and string.count(',') <= 1
                        and result is not None
                        and result.group(0) != ""))
    
        def on_validate(P):
            return validate(P)    
        
        validation = self.frame4.register(validate)
        
        self.x1_input = Tk.Entry(self.frame4, width=10, font = self.FONT_TYPE, \
                                 validate="all", validatecommand=(validation, '%P'))
        self.x1_input.pack(side="top", fill=None, padx=10, pady=6)
        self.x2_input = Tk.Entry(self.frame4, width=10, font = self.FONT_TYPE, \
                                 validate="key", validatecommand=(validation, '%S'))
        self.x2_input.pack(side="top", fill=None, padx=10, pady=6)
        self.y1_input = Tk.Entry(self.frame4, width=10, font = self.FONT_TYPE, \
                                 validate="key", validatecommand=(validation, '%S'))
        self.y1_input.pack(side="top", fill=None, padx=10, pady=6)
        self.y2_input = Tk.Entry(self.frame4, width=10, font = self.FONT_TYPE, \
                                 validate="key", validatecommand=(validation, '%S'))
        self.y2_input.pack(side="top", fill=None, padx=10, pady=6)
        
        self.line_check = Tk.Checkbutton(self.frame4, font = self.FONT_TYPE, var=True)
        self.line_check.select()
        self.line_check.pack(side="top", fill=None, padx=10, pady=5)
        self.marker_check = Tk.Checkbutton(self.frame4, font = self.FONT_TYPE)
        self.marker_check.select()
        self.marker_check.pack(side="top", fill=None, padx=10, pady=5)
    