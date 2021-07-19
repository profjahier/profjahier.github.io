from graphviz import Digraph # Ce module permet de dessiner des graphes orientés (Digraph)
from random import choice

class Graphe():  # graphe représenté par un Dictionnaire d'Adjacence
    """ Graphe implémenté à l'aide d'un dictionnaire d'adjacence.
    Exemple : 
    self.dico = {'sommet_x': {'sommet_y' : poids_xy, 'sommet_z' : poids_xz},  etc...}
    Chaque sommet est identifié par son étiquette (qui doit être unique !).
    """
    def __init__(self):
        """ Initialisation avec un graphe vide. """
        self.dico = dict()
    
    def ajouter_sommet(self, sommet):
        """ Ajoute un nouveau sommet au graphe. """
        if not sommet in self.dico:
            self.dico[sommet] = dict()
    
    def ajouter_arete(self, sommet1, sommet2, poids=1):
        """ Ajoute une arête au graphe de sommet1 vers sommet2.
        Si poids n'est pas renseigné, il prendra la valeur 1 par défaut. """
        # Si les sommets n'existent pas, on les crée avant l'arête :
        self.ajouter_sommet(sommet1)
        self.ajouter_sommet(sommet2)
            # On crée la connexion sommet1 -> sommet2 (arc orienté par défaut)
        self.dico[sommet1][sommet2] = poids
    
    def sommets(self):
        """ Renvoie la liste des sommets triée par étiquette. """
        return sorted(list(self.dico.keys()))
    
    def successeurs(self, sommet):
        """ Renvoie la liste des successeurs de sommet, triée par étiquette. """
        return sorted(list(self.dico[sommet].keys()))
    
    def poids(self, sommet1, sommet2):
        """ Renvoie le poids de l'arête sommet1->sommet2 ou 0 si pas d'arête. """
        if sommet2 not in self.dico[sommet1]:
            return 0
        else:
            return self.dico[sommet1][sommet2]
            
    def get_graphe(self):
        """ Renvoie le dictionnaire d'adjacence représentant le graphe. """
        return self.dico
    def set_graphe(self, dico):
        """ Définit le dictionnaire d'adjacence représentant le graphe. """
        self.dico = dico
    
    def parcours_profondeur(self, depart):
        """ Parcourt l'arbre en profondeur (DFS) """
        def dfs(sommet):
            traités.append(sommet)
            for successeur in self.successeurs(sommet):
                if successeur not in traités:
                    dfs(successeur)
        traités = []  # sommets déjà traités
        dfs(depart)
        return traités

    def parcours_largeur(self, depart):
        """ Parcourt l'arbre en largeur (BFS) """
        decouverts = [depart]  # sommets déjà decouverts
        file = [depart]
        while file:    # tant que la file n'est pas vide
            sommet = file.pop(0)
            for successeur in self.successeurs(sommet):
                if successeur not in decouverts:
                    file.append(successeur)
                    decouverts.append(successeur)
        return decouverts 
    
    def cycle(self):
        """ Renvoie True (resp. False) si le graphe contient (resp. ne contient pas) un cycle :
        Parcourt le graphe en largeur depuis un sommet quelconque et cherche si on retombe sur le sommet de départ """
        depart = choice(self.sommets())
        traités = []
        file = [depart]
        while file:    # tant que la file n'est pas vide
            sommet = file.pop(0)
            if sommet in traités:
                return True # on peut quitter la fonction : cycle trouvé !
            else:
                traités.append(sommet)
                for successeur in self.successeurs(sommet):
                    if successeur not in traités:
                        file.append(successeur)
        return False  # aucun cycle n'a été détecté
    
    def existe_chemin(self, depart, arrivee):
        """ Renvoie True si un chemin existe entre depart et arrivee,
        et donne un exemple de chemin possible (pas forcémetn unique) """
        def chemins(graphe, depart):
            """ Repose sur un parcourt l'arbre en largeur (BFS) """
            decouverts = [depart]  # sommets déjà visités
            file = [depart]
            trajets = {depart:[depart]}
            while file:    # tant que la pile n'est pas vide
                sommet = file.pop(0)
                for successeur in graphe.successeurs(sommet):
                    if successeur not in decouverts:
                        file.append(successeur)
                        decouverts.append(successeur)
                        trajets[successeur] = trajets[sommet] + [successeur]
            return trajets
        
        trajets = chemins(self, depart)
        if arrivee in trajets.keys():
            #print(trajets[arrivee]) # facultatif évidemment
            return True
        else:
            return False    

def dessiner(graphe, moteur='dot'):
    """Représentation graphique avec graphviz.
        Graphe doit avoir :
        - methode get_graphe() : renvoie le dictionnaire d'adjacence représentant le graphe.
        - méthode sommets() : renvoie la liste des sommets.
        - methode poids(s1, s2) : renvoie le poids d'un arc du sommet s1 vers le sommet s2, ou 0 si aucun arc
        Complément : moteur est le moteur de rendu de dot : au choix parmi dot (par défaut) circo, neato, fdp, osage, twopi, patchwork.
    """
    dot = Digraph(comment="Graphe orienté", format='png')
    dot.engine = moteur
    for sommet in graphe.sommets():
        dot.node(str(sommet), str(sommet))
        for (successeur, poids) in graphe.get_graphe()[sommet].items():
            # Teste si l'arête est orientée
            if graphe.poids(successeur, sommet) == graphe.poids(sommet, successeur) :
                # dessin d'une arête non orientée
                if successeur < sommet: # astuce pour ne dessiner qu'une seule arête entre les 2 sommets
                    if poids != 1 and poids != 0: # cas du graphe pondéré
                        dot.edge(str(sommet), str(successeur), label=str(poids), dir="none")
                    elif poids != 0: # pas d'arc entre les sommets
                        dot.edge(str(sommet), str(successeur), dir="none")
            else:
                # dessin d'une arête orientée
                if poids != 1 and poids != 0: # cas du graphe pondéré
                    dot.edge(str(sommet), str(successeur), label=str(poids))
                elif poids != 0: # pas d'arc entre les sommets
                    dot.edge(str(sommet), str(successeur))
    return dot

def mat2dico(matrice, etiquettes=None):
    """ Crée un dico d'adjacence à partir d'une matrice d'adjacence :
     - etiquettes est la liste des étiquettes des sommets 
    """
    n = len(matrice)
    if etiquettes is None: # si aucune étiquette de sommets communiquée :
        etiquettes = [i for i in range(n)] # on crée des sommets étiquettés de 0 à n-1
    assert len(etiquettes) == len(set(etiquettes)), "Erreur : doublon d'identifiants de sommets"
    dico = dict() 
    for i in range(n):
        dico[etiquettes[i]] = dict()
        for j in range(n):
            if matrice[i][j] != 0:  # 2 sommets non connectés sont séparés d'une distance nulle
                dico[etiquettes[i]][etiquettes[j]] = matrice[i][j]
    return dico