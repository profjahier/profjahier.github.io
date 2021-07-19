""" 
Module pour créer ou simplement visualiser des arbres binaires 
Dernière MAJ : 15 juillet 2021.
"""

from graphviz import Graph # Ce module permet de dessiner des arbres et des graphes
from math import floor, log
 
def dessiner(arbre):
        """ 
        Renvoie un objet graphviz pour la visualisation graphique d'un arbre binaire.
        Arbre doit avoir l'attribut suivant :
        - racine : noeud racine de l'arbre (type Noeud)
        Noeud a 3 attributs :
        - valeur : étiquette du noeud
        - gauche : fils gauche (un noeud ou None)
        - droit : fils droit (un noeud ou None)
        """
        def construction(dot, noeud):
            # Ajoute la représentation du noeud à la représentation dot de l'arbre
            if noeud is not None:
                dot.node(str(id(noeud)), str(noeud.valeur))
                # Appel récursif de la fonction construction
                if noeud.gauche is not None:
                    construction(dot, noeud.gauche)
                    if noeud.droit is not None: # il y a aussi un fils droit
                        dot.edge(str(id(noeud)) , str(id(noeud.gauche)))
                    else: # comme il n'y a pas de fils droit, on écrit '<' sur l'arête pour savoir que c'est un fils gauche
                        dot.edge(str(id(noeud)) , str(id(noeud.gauche)), '<')
                if noeud.droit is not None:
                    construction(dot, noeud.droit)
                    if noeud.gauche is not None: # il y a aussi un fils gauche
                        dot.edge(str(id(noeud)) , str(id(noeud.droit)))
                    else: # comme il n'y a pas de fils gauche, on écrit '>' sur l'arête pour savoir que c'est un fils droit
                        dot.edge(str(id(noeud)) , str(id(noeud.droit)), '>')
        
        if arbre.racine is None:
            print("Le graphe est vide...")
        else:
            dot = Graph(comment="Arbre binaire", format='png')
            construction(dot, arbre.racine)
            return dot
        
        
def tableau2arbre(tableau):
        """ 
        Construit un arbre à partir d'un tableau 'récursif' du type ["Noeud", [S_A_G], [S_A_D]].
        [ ] désigne un arbre vide.
        """
        def construction(tableau):
            if tableau != []: # arbre vide
                noeud = Noeud(tableau[0])
                noeud.gauche = construction(tableau[1])
                noeud.droit  = construction(tableau[2])
                return noeud
        
        return Arbrebin(construction(tableau))
    
    
class Noeud():
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        
    def __str__(self):
        return f"{self.valeur} (g[{self.valeur}] = {self.gauche}, d[{self.valeur}] = {self.droit})"
    
    def est_feuille(self):
        return self.gauche is None and self.droit is None
    
    def taille(self):
        if self.est_feuille():
            return 1
        n = 1
        if self.gauche is not None:
             n += self.gauche.taille()
        if self.droit is not None:
             n += self.droit.taille()
        return n
    
    def hauteur(self):
        if self.est_feuille():
            return 1
        hg, hd = 0, 0 # hauteur du sag et sad s'ils sont vides
        if self.gauche is not None:
             hg = self.gauche.hauteur()
        if self.droit is not None:
             hd = self.droit.hauteur()
        return 1 + max(hg, hd)
    
    def prefixe(self):
        """ Retourne la liste des valeurs noeuds dans un parcours en profondeur préfixe """
        if self.est_feuille():
            return [self.valeur]
        pg, pd = [], [] # parcours du sag et sad s'ils sont vides
        if self.gauche is not None:
             pg = self.gauche.prefixe()
        if self.droit is not None:
             pd = self.droit.prefixe()
        return [self.valeur] + pg + pd
    
    def infixe(self):
        """ Retourne la liste des valeurs noeuds dans un parcours en profondeur infixe """
        if self.est_feuille():
            return [self.valeur]
        pg, pd = [], []
        if self.gauche is not None:
             pg = self.gauche.infixe()
        if self.droit is not None:
             pd = self.droit.infixe()
        return pg + [self.valeur] + pd
    
    def suffixe(self):
        """ Retourne la liste des valeurs noeuds dans un parcours en profondeur suffixe """
        if self.est_feuille():
            return [self.valeur]
        pg, pd = [], []
        if self.gauche is not None:
             pg = self.gauche.suffixe()
        if self.droit is not None:
             pd = self.droit.suffixe()
        return pg + pd + [self.valeur] 
    
    def largeur(self):
        """ Retourne la liste des valeurs noeuds dans un parcours en largeur """
        liste = []
        file = [self]
        while file:
            noeud = file.pop(0)
            liste.append(noeud.valeur)
            if noeud.gauche is not None:
                 file.append(noeud.gauche)
            if noeud.droit is not None:
                 file.append(noeud.droit)
        return liste
    
    def inserer(self, valeur):
        """ Insère valeur en respectant les règles d'un ABR spécifiquement """
        if valeur < self.valeur:
            if self.gauche is None:
                self.gauche = Noeud(valeur)
            else:
                self.gauche.inserer(valeur)
        elif valeur > self.valeur:
            if self.droit is None:
                self.droit = Noeud(valeur)
            else:
                self.droit.inserer(valeur)
        else:
            assert False, "Pas de doublon dans un ABR !"
            
    def rechercher(self, valeur):
        """ Recherche valeur en respectant les contraintes d'un ABR. """
        if valeur < self.valeur:
            if self.gauche is None:
                return False
            else:
                return self.gauche.rechercher(valeur)
        elif valeur > self.valeur:
            if self.droit is None:
                return False
            else:
                return self.droit.rechercher(valeur)
        else:
            return True
    
    def ajoute_noeud_visu(self, graphe, parent=None, etiquette=None):
        """ Méthode récupérée sur Eduscol REssources Terminale 
        IMPLANTATION DES ARBRES BINAIRES DE RECHERCHE À L’AIDE DE LA POO
        """
        noeud = str(self.valeur)        
        graphe.node(noeud)        
        if not(parent is None):            
            graphe.edge(parent, noeud, label=etiquette)        
        if not(self.gauche is None):            
            self.gauche.ajoute_noeud_visu(graphe, noeud, "<")        
        if not(self.droit is None):            
            self.droit.ajoute_noeud_visu(graphe, noeud, ">")

        
class Arbrebin:
    def __init__(self, racine=None):
        self.racine = racine

    def __str__(self):
        return str(self.racine)
    
    def est_vide(self):
        return self.racine is None
    
    def taille(self):
        if self.est_vide():
            return 0
        else:
            return self.racine.taille()
        
    def hauteur(self):
        if self.est_vide():
            return 0
        else:
            return self.racine.hauteur()
    
    def prefixe(self):
        if self.est_vide():
            return []
        else:
            return self.racine.prefixe()
    
    def infixe(self):
        if self.est_vide():
            return []
        else:
            return self.racine.infixe()
    
    def suffixe(self):
        if self.est_vide():
            return []
        else:
            return self.racine.suffixe()
    
    def largeur(self):
        if self.est_vide():
            return []
        else:
            return self.racine.largeur()
        
    def est_ABR(self):
        """ Indique si l'arbre correspond bien à un arbre binaire de recherche :
        Dans ce cas son parcours en profondeur infixe doit être trié. """
        parcours_infixe = self.infixe()
        parcours_trié = sorted(parcours_infixe)
        return parcours_infixe == parcours_trié
    
    def inserer(self, valeur):
        """ Insère valeur dans l'arbre en respectant les contraintes des ABR. """
        if self.est_vide():
            self.racine = Noeud(valeur)
        elif self.est_ABR():
            self.racine.inserer(valeur)
        else:
            assert False, "L'arbre n'est pas un arbre binaire de recherche !"
        
    def h_min_max(self):
        """ Renvoie la hauteur mini et maxi possible de l'arbre en fonction de sa taille """
        n = self.taille()
        return (1 + floor(log(n, 2)), n)
    
    def rechercher(self, valeur):
        """ Recherche valeur dans l'arbre en respectant les contraintes d'un ABR. """
        if self.est_vide():
            return False
        elif self.est_ABR():
            return self.racine.rechercher(valeur)
        else:
            assert False, "La recherche ne peut s'effectuer que dans un arbre binaire de recherche !"
            
    def visu(self):        
        """ Méthode récupérée sur Eduscol REssources Terminale 
        IMPLANTATION DES ARBRES BINAIRES DE RECHERCHE À L’AIDE DE LA POO
        """
        if self.est_vide():
            print("Le graphe est vide...")     
        else:
            graphe = Graph(format='png')   
            self.racine.ajoute_noeud_visu(graphe)        
            graphe.render("Arbre", view=True)