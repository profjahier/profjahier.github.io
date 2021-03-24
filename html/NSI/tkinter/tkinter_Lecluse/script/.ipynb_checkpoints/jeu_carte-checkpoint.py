#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""

import tkinter as tk
from PIL import Image, ImageTk

# Variables globales
LARGEUR, HAUTEUR = 292, 296
no_image = 1 # No de carte

def change_carte(event):
    """Changement de carte si clic sur la carte"""
    global no_image, image_gif
    # On verifie que le clic a eu lieu sur la carte
    if 50 < event.x < 242 and 10 < event.y < 286:
        no_image = no_image % 8 + 1 # echange du no de carte
        imgPIL = Image.open("carte" + str(no_image) + ".png") # charge le fichier image avec PIL
        imgTk = ImageTk.PhotoImage(imgPIL) # transforme cette image en image utilisable pour Tkinter
        # On charge la nouvelle image
        surface_dessin.itemconfigure(ma_carte, image=imgTk)
        mon_app.update()

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Jeu de carte')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width=LARGEUR, height=HAUTEUR, bg='green')
surface_dessin.grid(column=0, row=0)

# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la surface provoquera l'appel de la fonction clic()
surface_dessin.bind('<Button-1>', change_carte)

imgPIL = Image.open("carte1.png") # charge le fichier image avec PIL
imgTk = ImageTk.PhotoImage(imgPIL) # transforme cette image en image utilisable pour Tkinter


# Bouton quitter
tk.Button(mon_app, text='Quitter', command=mon_app.destroy).grid(column=0, row=1)

# Placement de l'image initiale designee par "ma_carte" sur le canvas
ma_carte = surface_dessin.create_image((50, 10), image=imgTk, anchor="nw")

mon_app.mainloop()