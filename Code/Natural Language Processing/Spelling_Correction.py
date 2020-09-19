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

import Spelling_Correction_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Spelling_Correction_support.init(root, top)
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
    Spelling_Correction_support.init(w, top, *args, **kwargs)
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

        top.geometry("600x450+416+168")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("Spelling Correction")
        top.configure(highlightcolor="black")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.283, rely=0.0, relheight=0.111
                , relwidth=0.438)
        self.Message1.configure(font="-family {DejaVu Sans} -size 20")
        self.Message1.configure(foreground="#0000ff")
        self.Message1.configure(text='''Spelling Correction''')
        self.Message1.configure(width=263)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.317, rely=0.822, height=30, width=225)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Spelling Checker using Bigrams''')
	self.Button1.configure(command=lambda: call(["python3","Spelling_Correction/Spelling_Checker_using_Bigrams.py"]))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.317, rely=0.911, height=30, width=225)
        self.Button2.configure(activebackground="#f9f9f9")
        self.Button2.configure(text='''Spelling Checker using Trigrams''')
	self.Button2.configure(command=lambda: call(["python3","Spelling_Correction/Spelling_Checker_using_Trigrams.py"]))

        self.Message2 = tk.Message(top)
        self.Message2.place(relx=0.04, rely=0.133, relheight=0.640
                , relwidth=0.922)
        self.Message2.configure(font="-family {DejaVu Sans} -size 10")
        self.Message2.configure(text='''Spelling Correction is a process of detecting and correcting the incorrectly spelled words in a text.

Spell Checker is an application program that finds the incorrectly spelled words in a document and corrects them automatically.

When some text is given as an input to spell checker, it finds the incorrect words by checking their availability in the dictionary. Finally, it corrects these incorrect words using the N grams model.''')
        self.Message2.configure(width=553)

if __name__ == '__main__':
    vp_start_gui()





