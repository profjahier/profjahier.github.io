#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""

import tkinter as tk
from random import randint

nb_6 = 0
nb_total = 0

def nouveau_lance():
    global nb_6, nb_total
    nb = randint(1, 6)
    nb_total += 1
    if nb == 6:
        nb_6 += 1
    texte_de.set('Résultat -> ' + str(nb))
    texte_stats.set(f"{nb_6} // {nb_total}")

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Dé à 6 faces')

# Création d'un widget Button (bouton Lancer)
bouton_lancer = tk.Button(mon_app, text='Lancer', command=nouveau_lance)

# Positionnement du widget avec la méthode pack()
bouton_lancer.grid(column=0, row=0)

# Création d'un widget Button (bouton Quitter)
bouton_quitter = tk.Button(mon_app, text='Quitter', command=mon_app.destroy)
bouton_quitter.grid(column=0, columnspan=3, row=1, sticky='ew')

# Objet texte variable pour actualiser le texte du label
texte_de = tk.StringVar()
texte_stats = tk.StringVar()

# On appellle une fois la fonction pour initialiser notre texte_de
# cette sera ensuite appelée via le bouton "Lancer"
nouveau_lance()

# Création d'un widget Label dont le texte est variable
label_resultat = tk.Label(mon_app, textvariable = texte_de, fg='red', bg='white')
label_resultat.grid(column=1, row=0, padx=5)
label_stat = tk.Label(mon_app, textvariable=texte_stats, fg='blue', bg='white')
label_stat.grid(row=0, column=2)
mon_app.mainloop()