#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""

import tkinter as tk
from random import randint

def nouveau_lance():
    nb = randint(1, 6)
    texte_de.set('Résultat -> ' + str(nb))

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Dé à 6 faces')

# Création d'un widget Button (bouton Lancer)
bouton_lancer = tk.Button(mon_app, text = 'Lancer', command = nouveau_lance)

# Positionnement du widget avec la méthode grid()
bouton_lancer.grid(row=0, column=0)

# Création d'un widget Button (bouton Quitter)
bouton_quitter = tk.Button(mon_app, text ='Quitter', command = mon_app.destroy)
bouton_quitter.grid(row=1, column=0, columnspan=2, sticky='ew')

# Objet texte variable pour actualiser le texte du label
texte_de = tk.StringVar()

# On appellle une fois la fonction pour initialiser notre texte_de
# cette sera ensuite appelée via le bouton "Lancer"
nouveau_lance()

# Création d'un widget Label dont le texte est variable
label_resultat = tk.Label(mon_app, textvariable = texte_de, fg = 'red', bg = 'white')
label_resultat.grid(row=0, column=1)
mon_app.mainloop()