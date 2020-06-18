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

import Sentiment_Analysis_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Sentiment_Analysis_support.init(root, top)
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
    Sentiment_Analysis_support.init(w, top, *args, **kwargs)
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

        top.geometry("600x450+406+176")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(highlightcolor="black")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.25, rely=-0.022, relheight=0.133
                , relwidth=0.475)
        self.Message1.configure(font="-family {DejaVu Sans} -size 20")
        self.Message1.configure(foreground="#0000ff")
        self.Message1.configure(text='''Sentiment Analysis''')
        self.Message1.configure(width=285)

        self.Message2 = tk.Message(top)
        self.Message2.place(relx=0.017, rely=0.111, relheight=0.711
                , relwidth=0.972)
        self.Message2.configure(font="-family {DejaVu Sans} -size 10")
        self.Message2.configure(text='''Sentiment Analysis is a text categorization task. It is the extraction of sentiment i.e. the positive or negative orientation that a writer expresses toward some object.

A review of a lecture, book, or product on the web expresses the student’s sentiment toward the product.

Naive Bayes text classification can work well for sentiment analysis. We train naive Bayes classifiers using all words in the training set to estimate positive and negative sentiment.''')
        self.Message2.configure(width=583)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.333, rely=0.889, height=28, width=195)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Analyse Student Feedbacks''')
	self.Button1.configure(command=lambda: call(["python3","Sentiment_Analysis/Sentiment_Analysis_code.py"]))

if __name__ == '__main__':
    vp_start_gui()

