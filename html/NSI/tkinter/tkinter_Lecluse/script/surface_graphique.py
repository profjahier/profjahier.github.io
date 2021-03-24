#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""
import tkinter as tk
import random

# Constantes
LARGEUR = 480
HAUTEUR = 320

def dessine_cercle():
    """ Dessine un cercle de centre (x,y) et de rayon r """
    x = random.randint(0, LARGEUR)
    y = random.randint(0, HAUTEUR)
    r = 20
    surface_dessin.create_oval(x-r, y-r, x+r, y+r, outline='blue', fill='blue')

def effacer():
    """ Efface la zone graphique """
    surface_dessin.delete(tk.ALL)

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Cercle')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width = LARGEUR, height = HAUTEUR, bg = 'white')
surface_dessin.grid(row=0, column=0, columnspan=3)

# Création d'un widget tk.Button (bouton Go)
bouton_go = tk.Button(mon_app, text ='Go', command = dessine_cercle)
bouton_go.grid(row=1, column=0)


# Création d'un widget tk.Button (bouton Effacer)
bouton_effacer = tk.Button(mon_app, text ='Effacer', command = effacer)
bouton_effacer.grid(row=1, column=1)


# Création d'un widget tk.Button (bouton Quitter)
bouton_quitter = tk.Button(mon_app, text ='Quitter', command = mon_app.destroy)
bouton_quitter.grid(row=1, column=2)


mon_app.mainloop()