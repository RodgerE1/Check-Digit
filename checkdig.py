from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = int(inputnum.get())
        check.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root = Tk()
root.title("Check")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

inputnum = StringVar()
check = StringVar()

inputnum_entry = ttk.Entry(mainframe, width=17, textvariable=inputnum)
inputnum_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=check).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Enter 11 Digits").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Check Digit").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="check").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

inputnum_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()