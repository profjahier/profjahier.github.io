# tuto partie 3 : barres de défilement
import tkinter as tk
import tkinter.ttk as ttk

def afficher_position(evt):
    pos_x, pos_y = evt.x, evt.y
    affichage = f"Position : abscisse = {pos_x} ; ordonnées = {pos_y}"
    strvar_position.set(affichage)

appli = tk.Tk()
appli.title("Position de la souris dans un Canvas")

barre_horizontale = ttk.Scrollbar(appli, orient=tk.HORIZONTAL)
barre_horizontale.grid(row=11, column=10, sticky=('e', 'w'))
barre_verticale = ttk.Scrollbar(appli, orient=tk.VERTICAL)
barre_verticale.grid(row=10, column=11, sticky=('n', 's'))

can = tk.Canvas(appli, width=500, height=300, bg='pink', scrollregion=(0, 0, 800, 550), yscrollcommand=barre_verticale.set, xscrollcommand=barre_horizontale.set)
can.grid(row=10, column=10)

barre_horizontale['command'] = can.xview
barre_verticale['command'] = can.yview

can.create_rectangle(0, 0, 500, 300, fill='red')

strvar_position = tk.StringVar()
strvar_position.set('Position de la souris')
ttk.Label(appli, textvariable=strvar_position).grid(row=20, column=10)

can.bind("<Button-1>", afficher_position)

appli.mainloop()
