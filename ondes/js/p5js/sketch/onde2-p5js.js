var pause = false;
var T = 0.51; // paramètre très critique
var lambda = 0.25;
var amp = 0.5;
var t = 0;

function setup(){
  var canvas1 = createCanvas(600, 300); // 1ère ligne obligatoire !
  canvas1.parent('sketch1');
  /* dispose le canvas dans le div avec id='sketch1'
  sinon, par défaut le sketch est en fin de doc html */
  frameRate(50); // en fonction de cette valeur des effets de stroboscopie apparaissent... c'est pénible à gérer.
  fill(255,0,0); // onde rouge
 }

function amplitude(A, T, phi_0){
  return A * cos(TWO_PI * t / T + phi_0);
}

function draw(){
  var rayon = 5; // taille des points dessinés
  var nb_pt;
  var pas = 5; // changer ce paramètre pour modifier la densité de points dessinés
  nb_pt = 0.9*width/pas;
  if (!pause){
    t += 1;
    background(0);
    for (var i=0; i<=nb_pt; i++){
      var A = (amp*height/2);
      var phi_0 = i*lambda;
      ellipse(0.05*width+pas*i, height/2 + amplitude(A, T, phi_0), rayon);
    }
  }
}

function keyPressed(){
  if (keyCode == 32){ // barre espace
    arret();
  }else if (keyCode == 38 && lambda>0.05){ // fleche haut
    lambda -= 0.05;
  }else if (keyCode == 40 && lambda<0.6){ // fleche bas
    lambda += 0.05;
  }else if (keyCode == 37 && T<0.52){ // fleche gauche
    T += 0.002;
  }else if (keyCode == 39 && T>0.50){ // fleche droite
    T -= 0.002;
  }else if (keyCode == 65 && amp<0.9){ // touche A
    amp += 0.05;
  }else if (keyCode == 90 && amp>0.1){ // touche Z
    amp -= 0.05;
  }
  print(T);
  return false; // au cas où le navigateur et/ou le système d'exploitation cause un pb.
}

function arret(){
  pause = !pause;
}
