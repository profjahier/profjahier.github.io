from graphviz import Digraph # Ce module permet de dessiner des graphes orientés

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