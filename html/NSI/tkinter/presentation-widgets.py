import tkinter as tk
import tkinter.ttk as ttk

from PIL import Image, ImageTk

#######################
# mise en forme de la fenêtre principale 'appli'
#######################
appli = tk.Tk()

largeurAppli, hauteurAppli = 1000, 800
largeurEcran, hauteurEcran= appli.winfo_screenwidth(), appli.winfo_screenheight()
coinX, coinY = (largeurEcran - largeurAppli) // 2, (hauteurEcran - hauteurAppli) // 2
geometrie = str(largeurAppli)+'x'+str(hauteurAppli)+'+'+str(coinX)+'+'+str(coinY)
appli.geometry(geometrie)


appli.title('Démo des widgets tkinter et tkinter.tkk')

#######################


# Frame
frameNW = ttk.Frame(appli, relief='sunken', borderwidth=2)
frameNW.grid(column=0, row=0)

# Label
label = ttk.Label(frameNW, text="Petit texte dans un label")
label.grid(row=0, column=0)

# Image (on crée un objet image pour l'utliser ailleurs...)
imgPIL = Image.open('img/icone1.png')
imgTk = ImageTk.PhotoImage(imgPIL)

# Label (multiligne + Image)
labelMulti = ttk.Label(frameNW, relief='raised', wraplength = 150, justify='left',
                       image=imgTk, compound='right',
                       text="Je suis un texte dans un label et je suis écrit (avec relief raised) sur plusieurs lignes car je suis trop long, et puis j'ai une image à côté de moi (à droite grâce à l'option compound='right')").grid(row=10, column=0)

# Button
affiche = True
def cacheLabel():
    global affiche
    label.grid_remove() if affiche else label.grid()
    affiche = not affiche
    
ttk.Button(frameNW, text="Magic !\tObservez le label à ma gauche", command=cacheLabel).grid(row=0, column=10)
ttk.Button(frameNW, text="QUITTER\n\nscticky='nsew' pour m'étendre",  command=appli.destroy).grid(row=10, column=10, sticky='nsew')

# Checkbutton
compris = tk.BooleanVar()
compris.set(False)
ttk.Checkbutton(frameNW, text="Compris ? Check ?", variable=compris).grid(row=20, columnspan=20, column=0)
def comprisOK():
    correction.grid(row=25, column=10, sticky='w', padx=2) if compris.get() else correction.grid_forget()

correction = ttk.Label(frameNW, text="Check Bro !")
ttk.Button(frameNW, text="correction", command=comprisOK).grid(row=25, column=0, sticky='e', padx=2)
##### Remarque : columnspan "se compte" avec la numérotation choisie pour les columns (ici de 10 en 10)

# Radiotbutton
choix = tk.IntVar()
choix.set(2) # 'Beaucoup' sera ainsi la sélection par défaut
for i, texte in enumerate(["Un peu", "Beaucoup", "Passionnément"]):
    ttk.Radiobutton(frameNW, text=texte, variable=choix, value=i+1).grid(row=40+10*i, column=10, sticky='w')
ttk.Label(frameNW, text="Le choix est de valeur :").grid(row=40, column=0)
ttk.Label(frameNW, textvariable=choix).grid(row=50, column=0, rowspan=20)

# Entry
texte = tk.StringVar()
texte.set("Entrez quelque chose")
saisie = ttk.Entry(frameNW, textvariable=texte, width=30)
saisie.grid(row=70, column=0)
ttk.Label(frameNW, textvariable=texte).grid(row=70, column=10)
def palindrome():
    texte.set(texte.get()[::-1])
def modif():
    saisie.delete(0, 'end')
    saisie.insert(0, 'nouvelle saisie')
    
ttk.Button(frameNW, text="Palindrome de la saisie", command=palindrome).grid(row=80, column=0, sticky='ew')
ttk.Button(frameNW, text="Modifie la saisie sans StringVar", command=modif).grid(row=80, column=10, sticky='ew')

# Combobox
semaine = tk.StringVar()
semaine.set('Saisie libre & Liste')
jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'ou le week-end']
liste1 = ttk.Combobox(frameNW, textvariable=semaine, values=jours)
liste1.grid(row=90, column=0, sticky='ew')
ttk.Label(frameNW, textvariable=semaine).grid(row=90, column=10)


# Frame pour mmontrer les notebook
frameNE = ttk.Frame(appli)
frameNE.grid(column=10, row=0, padx=10)
# Notebook
carnet = ttk.Notebook(frameNE)
page1 = ttk.Frame(carnet)
page2 = ttk.Frame(carnet)
page3 = ttk.Frame(carnet)
carnet.add(page1, text="Boutons")
carnet.add(page2, text="Thèmes")
carnet.add(page3, text="Canvas")
carnet.grid(row=0, column=0)

ttk.Button(page1, text="quitter", command=appli.destroy).grid(row=0, column=0)


listeThemes= tk.StringVar()
themeActuel= tk.StringVar()
def afficheThemes():
        listeThemes.set(style.theme_names())
        
def changeTheme():
    global themeNumero
    themes = style.theme_names()
    if themeNumero < len(themes)-1:
        themeNumero += 1
    else:
        themeNumero = 0
    style.theme_use(themes[themeNumero])
    themeActuel.set(themes[themeNumero])
                     
style= ttk.Style()
themeActuel.set(style.theme_use())
ttk.Button(page2, text="Thèmes dispos ?", command=afficheThemes).grid(row=0, column=0)
ttk.Label(page2, textvariable=listeThemes).grid(row=1, column=0)
themeNumero = 0
ttk.Button(page2, text="Changer de thème", command=changeTheme).grid(row=2, column=0)
ttk.Label(page2, textvariable=themeActuel).grid(row=3, column=0)

tableau = tk.Canvas(page3, width=200, height=300, bg="white")
tableau.grid(row=0, column=0)
tableau.create_oval(10, 70, 20, 80, fill="red")

tableau.create_oval(50, 70, 60, 80, fill="blue")










appli.mainloop()
