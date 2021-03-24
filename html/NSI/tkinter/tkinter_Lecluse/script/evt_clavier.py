#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""

import tkinter as tk

# Variables globales

## Constantes
LARGEUR = 480
HAUTEUR = 320
## Position initiale du pion
pos_x = 230
pos_y = 150

def clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global pos_x, pos_y
    touche = event.char
    # déplacement vers le haut
    if touche == 'a':
        pos_y -= 20
    # déplacement vers le bas
    if touche == 'q':
        pos_y += 20
    # déplacement vers la droite
    if touche == 'm':
        pos_x += 20
    # déplacement vers le haut
    if touche == 'l':
        pos_x -= 20
    # on dessine le pion à sa nouvelle position
    surface_dessin.coords(pion, pos_x-10, pos_y-10, pos_x+10, pos_y+10)
    # Création de la fenêtre principale

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Clavier événement')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width=LARGEUR, height=HAUTEUR, bg='white')
surface_dessin.grid(row=0, column=0)
surface_dessin.focus_set()

# Création du pion sur la surface
pion = surface_dessin.create_oval(pos_x-10, pos_y-10, pos_x+10, pos_y+10, width=2, fill='red')

# La méthode bind() permet de lier un événement avec une fonction :
# un appui clavier provoquera l'appel de la fonction clavier()
surface_dessin.bind('<Key>', clavier)

# Création d'un widget Button (bouton Quitter)
tk.Button(mon_app, text = 'Quitter', command = mon_app.destroy).grid(row=1, column=0)

mon_app.mainloop()