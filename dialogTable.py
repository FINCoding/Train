from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

demos = {
    'Open': askopenfilename,
    'Color': askcolor,
    'Query': lambda: askquestion('Warning', 'Ypu tiped "rm *"\Confirm?'),
    'Error': lambda: showerror('Error!', 'He is dead, Jim'),
    'Input': lambda: askfloat('Entry', 'Enter credit card number')
}
