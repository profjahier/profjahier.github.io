#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""

import tkinter as tk

# Variables globales
LARGEUR, HAUTEUR = 240, 240
x1, y1 = 10, 10  # coordonnees initiales
dx, dy = 15, 0   # 'pas' du deplacement
flag =0          # indicateur de mouvement modifié par start_it et stop_it

def move():
    pass # nous allons la définir plus tard

def stop_it():
    """arret de l'animation"""
    global flag
    flag =0

def start_it():
    """demarrage de l'animation"""
    global flag
    if flag ==0:
        # pour ne lancer qu'une seule boucle
        flag =1
        move()

#========== Programme principal =============

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Animation')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width = LARGEUR, height = HAUTEUR, bg = 'white')
surface_dessin.pack(side = tk.LEFT, padx = 5, pady =5 )

# Creation de la balle. On memorise ici son nom, c'est important !!
bille = surface_dessin.create_oval(x1, y1, x1 + 30, y1 + 30, width = 2, fill = 'red')

tk.Button(mon_app,text='Quitter', width = 8, command=mon_app.destroy).pack(side=tk.BOTTOM)
tk.Button(mon_app, text='Demarrer', width = 8, command=start_it).pack()
tk.Button(mon_app, text='Arreter', width = 8, command=stop_it).pack()

# demarrage du receptionnaire d'evenements (boucle principale) :
mon_app.mainloop()