#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""
import tkinter as tk
# Variables globales
LARGEUR, HAUTEUR = 480, 320
x, y = 0,0
carre = 0
g = 1 # accélération

def move():
    """deplacement de la balle"""
    global x, y, g

    y += g
    g *= 1.15
    r = 20
    surface_dessin.coords(carre, x-r, y-r, x+r, y+r)
    if y < HAUTEUR - 2 * r:
        # => boucler apres 50 millisecondes si on est pas en bas
        surface_dessin.after(50, move)
    else:
        surface_dessin.coords(carre, x-r, HAUTEUR - 2 * r, x + r, HAUTEUR)

def clic(event):
    """ Gestion de l'événement Clic gauche sur la zone graphique """
    global x, y, carre, g

    g=1
    # position du pointeur de la souris
    x = event.x
    y = event.y
    # on dessine un carré
    r = 20
    # On cree le carre que l'on va animer
    carre = surface_dessin.create_rectangle(x-r, y-r, x+r, y+r, outline = 'black',fill = 'green')
    move()

def effacer():
    """ Efface la zone graphique """
    surface_dessin.delete(tk.ALL)

#========== Programme principal =============

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Carrés')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width = LARGEUR, height = HAUTEUR, bg = 'white')
surface_dessin.pack(side = tk.LEFT, padx = 5, pady =5 )

# Evenement clic sur la surface
surface_dessin.bind('<Button-1>', clic)

# Boutons
tk.Button(mon_app,text='Quitter', width = 8, command=mon_app.destroy).pack(side=tk.BOTTOM)
tk.Button(mon_app, text ='Effacer', command = effacer).pack()

# demarrage du receptionnaire d'evenements (boucle principale) :
mon_app.mainloop()