
var T = 0.3;
var pause = false;

var pas = 12;
var t = 0;

function setup(){
  var canvas1 = createCanvas(600, 300); // 1ère ligne obligatoire !
  canvas1.parent('sketch1');
  /* dispose le canvas dans le div avec id='sketch1'
  sinon, par défaut le sketch est en fin de doc html */
  frameRate(100);
 }

function amplitude(A, T, phi_0){
  return A * cos(360 * t / T + phi_0);
}

function draw(){
//  var A, T, phi_0;
  var rayon = 10;
//  var pas = 15;
  var nb_pt;
  nb_pt = 0.9*width/pas;
  if (!pause){
    t += 1;
    background(0);
    for (var i=0; i<=nb_pt; i++){
      var A = 50;
      var phi_0 = i;
      ellipse(0.05*width+pas*i, height/2 + amplitude(A, T, phi_0), rayon);
    }
  }
}

function mouseWheel(event){
  if (event.deltaY < 0){
    T += 0.05;
  }else{
    T -= 0.05;
  }
}

function keyPressed(){
  if (keyCode == 32){ // barre espace
    arret();
  }else if (keyCode == 38){ // fleche haut
    pas += 4;
  }else if (keyCode == 40){ // fleche bas
    pas -= 4;
  }
  return false; // au cas où le navigateur et/ou le système d'exploitation cause un pb.
}

function arret(){
  pause = !pause;
}
