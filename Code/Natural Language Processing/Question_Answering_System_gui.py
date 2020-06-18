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

import Question_Answering_System_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Question_Answering_System_support.init(root, top)
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
    Question_Answering_System_support.init(w, top, *args, **kwargs)
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
        top.title("Question Answer System")
        top.configure(highlightcolor="black")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.183, rely=0.0, relheight=0.111
                , relwidth=0.655)
        self.Message1.configure(font="-family {DejaVu Sans} -size 20")
        self.Message1.configure(foreground="#0000ff")
        self.Message1.configure(text='''Question Answer System''')
        self.Message1.configure(width=393)

        self.Message2 = tk.Message(top)
        self.Message2.place(relx=0.017, rely=0.133, relheight=0.644
                , relwidth=0.972)
        self.Message2.configure(text='''Question answering is the task of returning a particular piece of information to the user in response to a question.

There are many situations where the user wants a particular piece of information rather than an entire document or document set.

We call the task factoid question answering if the information is a simple fact, and particularly if this fact has to do with a named entity like a person, organization, or location.

The task of a factoid question answering system is thus to answer questions by finding, either from the Web or some other collection of documents, short text segments that are likely to contain answers to questions, reformatting them, and presenting them to the user.

The three phases of a modern factoid question answering system are :
1) Question processing
2) Passage retrieval and ranking
3) Answer processing''')
        self.Message2.configure(width=583)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.333, rely=0.844, height=28, width=187)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Find Answers to Questions''')
	self.Button1.configure(command=lambda: call(["python","Question_Answering_System/Question_Answering_System_code.py"]))

if __name__ == '__main__':
    vp_start_gui()

