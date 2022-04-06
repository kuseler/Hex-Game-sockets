from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
  
print("width x height = %d x %d (pixels)" %(monitor_width, monitor_height))
mainloop()
