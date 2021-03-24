#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""

import tkinter as tk

# Creation de la fenetre graphique
mon_app = tk.Tk()

# Creation des composants de la fenetre (widgets)
texte = tk.Label(mon_app, text='Bonjour tout le monde !', fg='red')
texte.grid(row=0, column=0)

bouton = tk.Button(mon_app, text='Quitter', command = mon_app.destroy)
bouton.grid(row=1, column=0)

# Lancement de l'application (boucle principale)
mon_app.mainloop()