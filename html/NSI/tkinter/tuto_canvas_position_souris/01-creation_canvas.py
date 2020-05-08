# tuto partie 1 : création du Canvas
import tkinter as tk
import tkinter.ttk as ttk

appli = tk.Tk()
appli.title("Position de la souris dans un Canvas")

can = tk.Canvas(appli, width=500, height=300, bg='pink')
can.grid(row=10, column=10)

appli.mainloop()
