/* Simulation d'une sinusoïdale
Possibillité de changer la longueur d'onde L ou la célérité V
Rappel : T = L / V
*/

var pause = false;
var V = 100;
var T;
var lambda = 100;
var amp = 0.5;
var img = 0;
var t;
var fps = 50;
var V_slider, L_slider, A_slider;

function setup(){
  var canvas1 = createCanvas(800, 400); // 1ère ligne obligatoire !
  canvas1.parent('sketch1');
  /* dispose le canvas dans le div avec id='sketch1'
  sinon, par défaut le sketch est en fin de doc html */
  frameRate(fps); // en fonction de cette valeur des effets de stroboscopie apparaissent... c'est pénible à gérer.
  fill(255,0,0); // onde rouge

  // création des sliders de contrôle
  V_slider = createSlider(10, 500, V, 10);
  L_slider = createSlider(0.1*width, 1.8*width, lambda, 10);
  A_slider = createSlider(0.1, 0.9, amp, 0.05);

  V_slider.parent('V_widget');
  L_slider.parent('L_widget');
  A_slider.parent('A_widget');

  V_slider.changed(maj);
  L_slider.changed(maj);
  A_slider.changed(maj);

  pause_btn = createButton('Pause');
  pause_btn.parent('widgets');
  pause_btn.mousePressed(arret);


  reset_btn = createButton('Reset');
  reset_btn.style('width', '200px');
  reset_btn.parent('widgets');
  reset_btn.mousePressed(raz);

 }

function draw(){
  var rayon = 5; // taille des points dessinés
  var nb_pt;
  var pas = 5; // changer ce paramètre pour modifier la densité de points dessinés
  nb_pt = 0.9*width/pas;
  if (!pause){
    img += 1;
  }
  t = img/fps;
  background(0);
  var A = amp*height/2;
  T = lambda / V;
  for (var point=0; point<=nb_pt; point++){
    var x = point*pas;
    var y = A * cos(TWO_PI * (t/T - x/lambda));
    ellipse(0.05*width + x, height/2 + y, rayon);
  }
  fill(255,0,255);
  textSize(20);
  text('V = '+V_slider.value()+' m/s'+'   L = '+L_slider.value()+' m'+'   A = '+A_slider.value()+' m', 50, 20);
  fill(255,0,0);
  }

function maj(){
  V = V_slider.value();
  lambda = L_slider.value();
  amp = A_slider.value();
}

function raz(){
  V_slider.value(100);
  L_slider.value(100);
  A_slider.value(0.5);
  maj();
}

function arret(){
  pause = !pause;
}
