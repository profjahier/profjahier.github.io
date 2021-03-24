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
texte1 = tk.Label(mon_app, text='Bonjour tout le monde !', fg='blue')
texte1.grid(row=0, column=0)

texte2 = tk.Label(mon_app, text="La NSI c'est super !!! !", bg='red')
texte2.grid(row=1, column=0)
bouton = tk.Button(mon_app, text='Au revoir', command = mon_app.destroy)
bouton.grid(row=2, column=0)

# Lancement de l'application (boucle principale)
mon_app.mainloop()