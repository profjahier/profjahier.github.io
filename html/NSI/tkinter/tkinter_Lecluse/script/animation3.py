#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""

import tkinter as tk

# Variables globales
LARGEUR, HAUTEUR = 240, 240
x1, y1 = 20, 20  # coordonnees initiales
dx, dy = 15, 0   # 'pas' du deplacement
flag =0          # indicateur de mouvement modifié par start_it et stop_it

def move():
    """deplacement de la balle"""
    global x1, y1, dx, dy, flag
    # On agit sur les coordonnées pour le mouvement de la balle
    x1, y1 = x1 + dx, y1 + dy
    if x1 > 190:
        x1 = 190
        dy = 15
    if y1 > 190:
        y1 = 190
        dx = -15
    if x1 < 20:
        x1 = 20
        dy = - 15
    if y1 < 20:
        y1 = 20
        dx = 15
    surface_dessin.coords(bille, x1, y1, x1+30, y1+30)
    # On gère le mouvement en rappelant la fonction move après 50 ms
    if flag == 1:
        surface_dessin.after(50, move)

def stop_it():
    """arret de l'animation"""
    global flag
    flag =0

def start_it():
    """demarrage de l'animation"""
    global flag
    if flag == 0:
        # pour ne lancer qu'une seule boucle
        flag = 1
        move()

#========== Programme principal =============

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Animation')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width=LARGEUR, height=HAUTEUR, bg='white')
surface_dessin.grid(row=0, column=0, columnspan=2)

# Creation de la balle. On memorise ici son nom, c'est important !!
bille = surface_dessin.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')

tk.Button(mon_app,text='Quitter', width=8, command=mon_app.destroy).grid(row=2, column=0, columnspan=2, sticky='ew')
tk.Button(mon_app, text='Demarrer', widt=8, command=start_it).grid(row=1, column=0)
tk.Button(mon_app, text='Arreter', width=8, command=stop_it).grid(row=1, column=1)

# demarrage du receptionnaire d'evenements (boucle principale) :
mon_app.mainloop()