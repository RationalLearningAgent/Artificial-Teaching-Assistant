from subprocess import call
import sys

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

import Grammar_Checker_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Grammar_Checker_support.init(root, top)
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
    Grammar_Checker_support.init(w, top, *args, **kwargs)
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

        top.geometry("600x450+461+158")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("Grammar Checker")
        top.configure(highlightcolor="black")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.183, rely=0.0, relheight=0.111
                , relwidth=0.655)
        self.Message1.configure(font="-family {DejaVu Sans} -size 20")
        self.Message1.configure(foreground="#0000ff")
        self.Message1.configure(text='''Grammar Checker''')
        self.Message1.configure(width=393)

        self.Message2 = tk.Message(top)
        self.Message2.place(relx=0.017, rely=0.133, relheight=0.644
                , relwidth=0.972)
        self.Message2.configure(text='''A grammar checker is a program that attempts to verify a written text for grammatical correctness.

The most commonly used mathematical system for modeling constituent structure in English and other natural languages is the Context Free Grammar (CFG).

A context free grammar consists of a set of rules or productions and a lexicon of words and symbols. Each rule or production expresses the ways in which the symbols of the language can be grouped and ordered together.

The symbols that are used in a CFG are divided into two classes : terminals and non terminals.

The symbols that correspond to words in the language (the,school etc) are called terminal symbols; the lexicon is the set of rules that introduce these terminal symbols.

The symbols that express clusters or generalizations of these are called nonterminals.''')
        self.Message2.configure(width=583)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.350, rely=0.844, height=28, width=187)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Check Grammar''')
	self.Button1.configure(command=lambda: call(["python3","Grammar_Checker/Grammar_Checker_main.py"]))

if __name__ == '__main__':
    vp_start_gui()





