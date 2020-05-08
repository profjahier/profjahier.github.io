# tuto partie 4 : détection souris dans l'espace visible et dans scrollregion
import tkinter as tk
import tkinter.ttk as ttk

def afficher_position(evt):
    pos_visible_x, pos_visible_y = evt.x, evt.y
    affichage_visible = f"Position visible : abscisse = {pos_visible_x} ; ordonnées = {pos_visible_y}"
    strvar_position_visible.set(affichage_visible)

    pos_scrollregion_x, pos_scrollregion_y = can.canvasx(evt.x), can.canvasy(evt.y)
    affichage_scrollregion = f"Position dans scrollregion : abscisse = {pos_scrollregion_x} ; ordonnées = {pos_scrollregion_y}"
    strvar_position_scrollregion.set(affichage_scrollregion)

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

strvar_position_visible = tk.StringVar()
strvar_position_visible.set('Position de la souris dans la zone visible')
ttk.Label(appli, textvariable=strvar_position_visible).grid(row=20, column=10)

strvar_position_scrollregion = tk.StringVar()
strvar_position_scrollregion.set('Position de la souris dans la scrollregion')
ttk.Label(appli, textvariable=strvar_position_scrollregion).grid(row=30, column=10)

can.bind("<Button-1>", afficher_position)

appli.mainloop()
