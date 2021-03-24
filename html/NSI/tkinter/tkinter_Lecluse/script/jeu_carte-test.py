#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""

import tkinter as tk

# Variables globales
LARGEUR, HAUTEUR = 292, 296
no_image = 1 # No de carte

def change_carte(event):
    """Changement de carte si clic sur la carte"""
    global no_image, imgtk
    # On verifie que le clic a eu lieu sur la carte
    if 50 < event.x < 242 and 10 < event.y < 286:
        no_image = no_image % 8 + 1 # echange du no de carte
        imgtk = tk.PhotoImage(file="carte" + str(no_image) + ".png")
        # On charge la nouvelle image
        surface_dessin.itemconfigure(ma_carte, image=imgtk)

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Jeu de carte')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width=LARGEUR, height=HAUTEUR, bg='white')
surface_dessin.grid(row=0, column=0)
# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la surface provoquera l'appel de la fonction clic()
surface_dessin.bind('<Button-1>', change_carte)
imgtk = tk.PhotoImage(file="carte1.png")

# Bouton quitter
tk.Button(mon_app, text = 'Quitter', command = mon_app.destroy).grid(row=1, column=0)

# Placement de l'image initiale designee par "ma_carte" sur le canvas
ma_carte = surface_dessin.create_image((50, 10), image=imgtk, anchor="nw")

mon_app.mainloop()