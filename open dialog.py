import tkinter as tk
from tkinter import filedialog
from tkinter import *


guiMain = tk.Tk()
guiMain.withdraw()
guiMain.fileName = filedialog.askopenfilename(filetypes=(('All picture files', '*.*')))
file_path = filedialog.askopenfilename()
