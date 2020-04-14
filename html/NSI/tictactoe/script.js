"use strict";

// paramètres du jeu 
const DIM = 3;
const VIDE = 0;
const CASE = 150;
const RAYON = 0.7 * CASE/2;
const JOUEURS = new Map([[1 , ['blue', 'bleu'] ],  [-1 , ['green', 'vert']]]); // dictionnaire
const NB_COUPS_MAX = DIM * DIM;
//****** fin paramètres  

//* Variables globales : pour faciliter la communication au seind des fonctions 
let status = document.getElementById('status');
let bouton = document.getElementById('bouton');
let canvas = document.querySelector('#plateau');
let plateau = canvas.getContext('2d'); // conserve une référence (Context) à la zone graphique pour 1 graphe 2D 
const largeur = canvas.width = CASE * DIM;
const hauteur = canvas.height = CASE * DIM;
let joueur = 1;
let grille = [];
let nb_coups = 0;
//******* fin variables globales 

function caseCliquee(evt){
    // récupère la position du clic sur le plateau et appelle la fonction jouer si la case est libre 
    let x = evt.offsetX; // Position de la souris par rapport à l'élément appelant
    let y = evt.offsetY;
    let c = Math.trunc(x / CASE);
    let l = Math.trunc(y / CASE);
    if (grille[l][c] == VIDE){
        jouer(l, c);
    }
}

function dessinerPion(l, c, couleur){
    // Dessine un pion dans la case (l, c) de la bonne couleur 
    plateau.fillStyle = couleur;
    plateau.beginPath();
    plateau.arc(CASE/2 + c*CASE, CASE/2 + l*CASE, RAYON, 0, 2*Math.PI, true);
    plateau.fill();
}

function jouer(l, c){
    // moteur principal du jeu 
    nb_coups++;
    let couleur = JOUEURS.get(joueur)[0];
    grille[l][c] = joueur; // maj de la grille
    dessinerPion(l, c, couleur);
    afficherGrille(); // retour console facultatif 
    if (gagnant()){
        canvas.removeEventListener("click", caseCliquee);
        status.textContent = "Gagnant : joueur "+ JOUEURS.get(joueur)[1]+" !!!";
        bouton.textContent = "Rejouer";
        bouton.setAttribute("onclick", "partie()");
        return
    }
    if (nb_coups == NB_COUPS_MAX){
        canvas.removeEventListener("click", caseCliquee);
        status.textContent = "Fin du jeu ! Match nul...";
        bouton.textContent = "Rejouer";
        bouton.setAttribute("onclick", "partie()");
        return
    }
    joueur = - joueur; // changement de joueur
}

function partie(){
    // Initialisation d'une nouvelle partie
    nb_coups = 0;
    bouton.textContent = "Partie en cours...";
    bouton.removeAttribute("onclick");
    status.textContent = "Cliquer sur une case pour jouer";
    grille = creerGrille(DIM, VIDE);
    canvas.addEventListener("click", caseCliquee);
    dessinerPlateau();
    afficherGrille(); // retour console facultatif 
}

function dessinerPlateau(evt) {
    plateau.clearRect(0, 0, largeur, hauteur); // nettoie tout le canvas 
    plateau.strokeStyle = 'red';
    for (let i = 0; i < DIM; i++) {
        plateau.beginPath();
        plateau.moveTo(0, CASE * i);
        plateau.lineTo(CASE * DIM, CASE * i);
        plateau.stroke();

        plateau.beginPath();
        plateau.moveTo(CASE * i, 0);
        plateau.lineTo(CASE * i, CASE * DIM);
        plateau.stroke();
    }
    plateau.strokeStyle = 'black';
    plateau.strokeRect(0, 0, largeur, hauteur);
}

function creerGrille(dim = 3, vide = 0) {
    // Renvoie une grille carrée de dimension 'dim', remplie de 'vide' 
    let grille = [];
    for (let i = 0; i < dim; i++) {
        let ligne = [];
        for (let j = 0; j < dim; j++) {
            ligne.push(vide);
        }
        grille.push(ligne);
    }
    return grille
}

function afficherGrille(){
    // Rendu graphique en console de la grille 
    console.log(grille);
}

dessinerPlateau();

function gagnant(){
// Renvoie true si le joueur gagne (sinon false)
    // ligne gagnante ?
    for (let l =0 ; l < DIM; l++){
        let c = 0;
        while (c < DIM && grille[l][c] == joueur){
            c++;
        }
        if (c == DIM){
            return true;
        }
    }
    // colonne gagnante ?
    for (let c =0 ; c < DIM; c++){
        let l = 0;
        while (l < DIM && grille[l][c] == joueur){
            l++;
        }
        if (l == DIM){
            return true;
        }
    }
    // diagonale 1 gagnante ?
    let n = 0;
    while (n < DIM && grille[n][n] == joueur){
        n++;
    }
    if (n == DIM){
        return true;
    }
    // diagonale 2 gagnante ?
    let m = 0;
    while (m < DIM && grille[m][DIM - 1 - m] == joueur){
        m++;
    }
    if (m == DIM){
        return true;
    }
    return false; // le joueur n'a pas gagné
}