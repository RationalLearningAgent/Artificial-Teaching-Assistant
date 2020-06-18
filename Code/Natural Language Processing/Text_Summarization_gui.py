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

import Text_Summarization_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Text_Summarization_support.init(root, top)
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
    Text_Summarization_support.init(w, top, *args, **kwargs)
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

        top.geometry("600x450+407+139")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("Text Summarization")
        top.configure(background="#d8d8d8")
        top.configure(highlightcolor="black")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.25, rely=0.0, relheight=0.111, relwidth=0.488)

        self.Message1.configure(font="-family {DejaVu Sans} -size 20")
        self.Message1.configure(foreground="#0000ff")
        self.Message1.configure(text='''Text Summarization''')
        self.Message1.configure(width=293)

        self.Message2 = tk.Message(top)
        self.Message2.place(relx=0.017, rely=0.133, relheight=0.756
                , relwidth=0.955)
        self.Message2.configure(anchor='n')
        self.Message2.configure(background="#d8d8d8")
        self.Message2.configure(font="-family {DejaVu Sans} -size 11")
        self.Message2.configure(text='''Text summarization is the process of distilling the most important information from a text to produce an abridged version for a particular task and user.

Applications :

Important kinds of summaries that are the focus of current research include :

1) Outlines of any document
2) Abstracts of a scientific article
3) Headlines of a news article
4) Summaries of email threads
5) Action items or other summaries of a (spoken) business meeting
6) Snippets summarizing a web page on a search engine results page
7) Compressed sentences for producing simplified or compressed text
8) Answers to complex questions, constructed by summarizing multiple documents''')
        self.Message2.configure(width=573)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.4, rely=0.889, height=28, width=126)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Summarize Text''')
	self.Button1.configure(command=lambda: call(["python3","Text_Summarization/Text_Summarization_code.py"]))

if __name__ == '__main__':
    vp_start_gui()

