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
        self.Message1.place(relx=0.0, rely=0.0, relheight=0.156, relwidth=1.005)
        self.Message1.configure(background="#fff9a3")
        self.Message1.configure(font="-family {DejaVu Sans} -size 20")
        self.Message1.configure(foreground="#ff0000")
        self.Message1.configure(highlightbackground="#0dc4d8")
        self.Message1.configure(highlightcolor="#55d813")
        self.Message1.configure(justify='center')
        self.Message1.configure(text='''Natural Language Processing (NLP)''')
        self.Message1.configure(width=601)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.05, rely=0.178, height=30, width=250)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(anchor='w')
        self.Button1.configure(text='''1. Spelling Correction''')
	self.Button1.configure(command=lambda: call(["python","Spelling_Correction/Spelling_Correction.py"]))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.05, rely=0.267, height=30, width=250)
        self.Button2.configure(activebackground="#f9f9f9")
        self.Button2.configure(anchor='w')
        self.Button2.configure(text='''2. Context Free Grammar Checker''')

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.05, rely=0.356, height=30, width=250)
        self.Button3.configure(activebackground="#f9f9f9")
        self.Button3.configure(anchor='w')
        self.Button3.configure(text='''3. Machine Translation''')

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.05, rely=0.444, height=30, width=250)
        self.Button4.configure(activebackground="#f9f9f9")
        self.Button4.configure(anchor='w')
        self.Button4.configure(text='''4. Information Retrieval''')

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.05, rely=0.533, height=30, width=250)
        self.Button5.configure(activebackground="#f9f9f9")
        self.Button5.configure(anchor='w')
        self.Button5.configure(text='''5. Question Answer System''')
	self.Button5.configure(command=lambda: call(["python","Question_Answering_System/Question_Answering_System.py"]))

        self.Button6 = tk.Button(top)
        self.Button6.place(relx=0.05, rely=0.622, height=30, width=250)
        self.Button6.configure(activebackground="#f9f9f9")
        self.Button6.configure(anchor='w')
        self.Button6.configure(text='''6. Categorization''')

        self.Button7 = tk.Button(top)
        self.Button7.place(relx=0.05, rely=0.711, height=30, width=250)
        self.Button7.configure(activebackground="#f9f9f9")
        self.Button7.configure(anchor='w')
        self.Button7.configure(text='''7. Text Summarization''')
	self.Button7.configure(command=lambda: call(["python","Text_Summarization/Text_Summarization.py"]))

        self.Button9 = tk.Button(top)
        self.Button9.place(relx=0.05, rely=0.8, height=30, width=250)
        self.Button9.configure(activebackground="#f9f9f9")
        self.Button9.configure(anchor='w')
        self.Button9.configure(text='''8. Sentiment Analysis''')
	self.Button9.configure(command=lambda: call(["python","Sentiment_Analysis/Sentiment_Analysis.py"]))

        self.Button8 = tk.Button(top)
        self.Button8.place(relx=0.05, rely=0.889, height=30, width=250)
        self.Button8.configure(activebackground="#f9f9f9")
        self.Button8.configure(anchor='w')
        self.Button8.configure(text='''9. Named Entity Recognition (NER)''')

if __name__ == '__main__':
    vp_start_gui()

