#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:52:20 2021

@author: profjahier
"""
import tkinter as tk
import tkinter.messagebox as msgb # boîte de dialogue

def verification():
    if mot_de_passe.get() == 'python':
        # le mot de passe est bon :
        # on affiche une boîte de dialogue puis on ferme la fenêtre
        msgb.showinfo('Résultat','Mot de passe correct.\nAu revoir !')
        mon_app.destroy()
    else:
        # le mot de passe est incorrect : on affiche une boîte de dialogue
        msgb.showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')
        mot_de_passe.set('')

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Identification requise')

# Création d'un widget Label (texte 'Mot de passe')
texte1 = tk.Label(mon_app, text='Mot de passe ')
texte1.grid(row=0, column=0)

# Création d'un widget Entry (champ de saisie)
mot_de_passe = tk.StringVar()
ligne_saisie = tk.Entry(mon_app, textvariable=mot_de_passe, show='*', bg='bisque', fg='maroon')
ligne_saisie.focus_set()
ligne_saisie.grid(row=0, column=1)

# Création d'un widget Button (bouton Valider)
tk.Button(mon_app, text='Valider', command=verification).grid(row=0, column=2)

mon_app.mainloop()