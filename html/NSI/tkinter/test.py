import tkinter as tk
import tkinter.ttk as ttk

from random import choice
    

def modifStatus():
    phrases = ["Je suis prêt", "Je fais l'action 1", "Encore en attente"]
    status_nouveau = choice(phrases) # choisit un status au hasard !
    status.set(status_nouveau) # l'affichage du Label s'actualise avec le nouveau status

def compteurIncrementer():
    compteur_actuel = compteur.get() # récupère la valeur actuelle de compteur
    compteur_nouveau = compteur_actuel + 1
    compteur.set(compteur_nouveau) # définit une nouvelle valeur pour le compteur


def themeChange():
    global style
    themes = list( style.theme_names() )
    theme = choice(themes)
    status.set(theme)
    style.theme_use(theme)
    


    
interface = tk.Tk()


status = tk.StringVar()
status.set("En attente...")

compteur = tk.IntVar()
compteur.set(1)

tk.Label(interface, textvariable=status).pack()
tk.Label(interface, textvariable=compteur).pack()

tk.Button(interface, text="changer de status", command=modifStatus).pack()
tk.Button(interface, text="incrémenter le compteur", command=compteurIncrementer).pack()


style = ttk.Style()
style.theme_use('clam')

    
ttk.Label(interface, textvariable=status).pack()
ttk.Label(interface, textvariable=compteur).pack()

ttk.Button(interface, text="changer de status", command=modifStatus).pack()
ttk.Button(interface, text="incrémenter le compteur", command=compteurIncrementer).pack()


ttk.Button(interface, text="changer de thème", command=themeChange).pack()


interface.mainloop()
