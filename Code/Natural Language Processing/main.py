import os
from subprocess import call
import sys

cwd=os.getcwd()
wd=cwd+"/Natural_Language_Processing"
os.chdir(wd)

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("602x450+410+158")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("Natural Language Processing (NLP)")
        top.configure(background="#9388d8")
        top.configure(highlightcolor="black")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.0, rely=0.0, relheight=0.200, relwidth=1.005)
        self.Message1.configure(background="#fff9a3")
        self.Message1.configure(font="-family {DejaVu Sans} -size 22")
        self.Message1.configure(foreground="#ff0000")
        self.Message1.configure(highlightbackground="#0dc4d8")
        self.Message1.configure(highlightcolor="#55d813")
        self.Message1.configure(justify='center')
        self.Message1.configure(text='''Natural Language Processing (NLP)''')
        self.Message1.configure(width=601)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.05, rely=0.250, relheight=0.100, relwidth=0.90)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(anchor='center')
	self.Button1.configure(font="size 12")
        self.Button1.configure(text='''Spelling Correction''')
	self.Button1.configure(command=lambda: call(["python","Spelling_Correction/Spelling_Correction.py"]))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.05, rely=0.400, relheight=0.100, relwidth=0.90)
        self.Button2.configure(activebackground="#f9f9f9")
        self.Button2.configure(anchor='center')
	self.Button2.configure(font="size 12")
        self.Button2.configure(text='''Grammar Checker''')
	self.Button2.configure(command=lambda: call(["python","Grammar_Checker/Grammar_Checker.py"]))

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.05, rely=0.550, relheight=0.100, relwidth=0.90)
        self.Button3.configure(activebackground="#f9f9f9")
        self.Button3.configure(anchor='center')
	self.Button3.configure(font="size 12")
        self.Button3.configure(text='''Question Answer System''')
	self.Button3.configure(command=lambda: call(["python","Question_Answering_System/Question_Answering_System.py"]))

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.05, rely=0.700, relheight=0.100, relwidth=0.90)
        self.Button4.configure(activebackground="#f9f9f9")
        self.Button4.configure(anchor='center')
	self.Button4.configure(font="size 12")
        self.Button4.configure(text='''Sentiment Analysis''')
	self.Button4.configure(command=lambda: call(["python","Sentiment_Analysis/Sentiment_Analysis.py"]))

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.05, rely=0.850, relheight=0.100, relwidth=0.90)
        self.Button5.configure(activebackground="#f9f9f9")
        self.Button5.configure(anchor='center')
	self.Button5.configure(font="size 12")
        self.Button5.configure(text='''Text Summarization''')
	self.Button5.configure(command=lambda: call(["python","Text_Summarization/Text_Summarization.py"]))

if __name__ == '__main__':
    vp_start_gui()





