import tkinter.filedialog

def data():
  with tkinter.filedialog.askopenfile() as f:
    d = f.read()
  return d