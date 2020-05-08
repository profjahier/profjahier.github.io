# tuto partie 5 : détection souris dans une grille
import tkinter as tk
import tkinter.ttk as ttk

def afficher_position(evt):
    pos_x, pos_y = can.canvasx(evt.x), can.canvasy(evt.y)
    strvar_position.set(f"Position du clic : abscisse = {pos_x} ; ordonnées = {pos_y}")

    colonne, ligne = pos_x // L, pos_y//H
    strvar_case.set(f"Case désignée : colonne = {int(colonne)} ; ligne = {int(ligne)}")


appli = tk.Tk()
appli.title("Position de la souris dans un Canvas")

NB_L = 10 # nombre de lignes dans la grille 
NB_C = 15# nombre de colonnes dans la grille 
L = 100 # largeur d'une case 
H = 70 # hauteur d'une case 
Lcan = NB_C * L # largeur du Canvas 
Hcan = NB_L * H # hauteur du Canvas 
print(Lcan, Hcan)

barre_horizontale = ttk.Scrollbar(appli, orient=tk.HORIZONTAL)
barre_horizontale.grid(row=11, column=10, sticky=('e', 'w'))
barre_verticale = ttk.Scrollbar(appli, orient=tk.VERTICAL)
barre_verticale.grid(row=10, column=11, sticky=('n', 's'))
can = tk.Canvas(appli, width=500, height=400, bg='pink', scrollregion=(0, 0, Lcan, Hcan), yscrollcommand=barre_verticale.set, xscrollcommand=barre_horizontale.set)
can.grid(row=10, column=10)
barre_horizontale['command'] = can.xview
barre_verticale['command'] = can.yview

for i in range(1, NB_L):
    can.create_line(0, i*H, Lcan, i*H, fill='blue')
for i in range(1, NB_C):
    can.create_line(i*L, 0, i*L, Hcan, fill='red')
for i in range(NB_L):
    for j in range(NB_C):
        can.create_text((j + 0.5) * L, (i + 0.5) * H, text=f"col = {j} \n\nlig = {i}")

strvar_position = tk.StringVar()
strvar_position.set('Position de la souris dans la scrollregion')
ttk.Label(appli, textvariable=strvar_position).grid(row=20, column=10)

strvar_case = tk.StringVar()
strvar_case.set('Case désignée')
ttk.Label(appli, textvariable=strvar_case).grid(row=30, column=10)

can.bind("<Button-1>", afficher_position)

appli.mainloop()
