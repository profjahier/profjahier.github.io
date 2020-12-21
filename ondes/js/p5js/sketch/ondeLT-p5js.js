/* Simulation d'une onde sinusoïdale
Possibillité de changer la longueur d'onde L ou la période T
Rappel : V = L / T (célérité V)
*/

var pause = false;
var T = 1; // paramètre très critique
var lambda = 100;
var amp = 0.5;
var img = 0;
var t;
var fps = 50;

function setup(){
  var canvas1 = createCanvas(600, 300); // 1ère ligne obligatoire !
  canvas1.parent('sketch1');
  /* dispose le canvas dans le div avec id='sketch1'
  sinon, par défaut le sketch est en fin de doc html */
  frameRate(fps); // en fonction de cette valeur des effets de stroboscopie apparaissent... c'est pénible à gérer.
  fill(255,0,0); // onde rouge
 }

function draw(){
  var rayon = 5; // taille des points dessinés
  var nb_pt;
  var pas = 5; // changer ce paramètre pour modifier la densité de points dessinés
  nb_pt = 0.9*width/pas;
  if (!pause){
    img += 1;
    t = img/fps;
    background(0);
    var A = amp*height/2;
    for (var point=0; point<=nb_pt; point++){
      var x = point*pas;
      var y = A * cos(TWO_PI * (t/T - x/lambda));
      ellipse(0.05*width  + x, height/2 + y, rayon);
    }
  }
}

function keyPressed(){
  if (keyCode == 32){ // barre espace
    arret();
  }else if (keyCode == 40 && lambda>0.1*width){ // fleche haut
    lambda -= 10;
  }else if (keyCode == 38 && lambda<1.8*width){ // fleche bas
    lambda += 10;
  }else if (keyCode == 39 && T<10){ // fleche gauche
    T += 0.1;
  }else if (keyCode == 37 && T>0.2){ // fleche droite
    T -= 0.1;
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
