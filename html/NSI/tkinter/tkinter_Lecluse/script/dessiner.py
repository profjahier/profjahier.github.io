#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""
import tkinter as tk

# Constantes
LARGEUR = 480
HAUTEUR = 320

# Variables globales
old_x, old_y = 0, 0

def clic(event):
    """ Gestion de l'événement clic gauche sur la zone graphique """
    global old_x, old_y
    # position du pointeur de la souris
    old_x = event.x
    old_y = event.y

def drag(event):
    global old_x, old_y
    x = event.x
    y = event.y
    surface_dessin.create_line(old_x, old_y, x, y, fill='green')
    old_x = event.x
    old_y = event.y

def effacer():
    """ Efface la zone graphique """
    surface_dessin.delete(tk.ALL)

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Dessiner')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width=LARGEUR, height=HAUTEUR, bg='white')
surface_dessin.grid(row=0, column=0, columnspan=2)

# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la surface provoquera l'appel de la fonction clic()
surface_dessin.bind('<Button-1>', clic)
surface_dessin.bind('<B1-Motion>', drag)

# Création d'un widget Button (bouton effacer)
tk.Button(mon_app, text='Effacer', command=effacer).grid(row=1, column=0, sticky='ew')
# Création d'un widget Button (bouton Quitter)
tk.Button(mon_app, text='Quitter', command=mon_app.destroy).grid(row=1, column=1, sticky='ew')

mon_app.mainloop()