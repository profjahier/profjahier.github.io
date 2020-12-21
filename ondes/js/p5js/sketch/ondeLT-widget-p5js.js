/* Simulation d'une onde sinusoïdale
Possibillité de changer la longueur d'onde L ou la période T
Rappel : V = L / T (célérité V)
*/

var pause = false;
var T = 1;
var lambda = 100;
var amp = 0.5;
var img = 0;
var t;
var fps = 50;
var T_slider, L_slider, A_slider;
var eclairage;

function setup(){
  var canvas1 = createCanvas(800, 400); // 1ère ligne obligatoire !
  canvas1.parent('sketch1');
  /* dispose le canvas dans le div avec id='sketch1'
  sinon, par défaut le sketch est en fin de doc html */
  frameRate(fps); // frame per second
  fill(255,0,0); // onde rouge

  // création des sliders de contrôle : createSlider(min, max, valeur_init, pas)
  T_slider = createSlider(0.2, 10, T, 0.1);
  L_slider = createSlider(0.1*width, 1.8*width, lambda, 10);
  A_slider = createSlider(0.1, 0.8, amp, 0.05);

  // positionnement des Sliders dans le DOM
  T_slider.parent('T_widget');
  L_slider.parent('L_widget');
  A_slider.parent('A_widget');

  // maj de la courbe lorsqu'un Slider est modifié par l'utilisateur
  T_slider.changed(maj);
  L_slider.changed(maj);
  A_slider.changed(maj);

  // bouton pause pour arrêter l'animation
  pause_btn = createButton('Pause');
  pause_btn.parent('widgets');
  pause_btn.mousePressed(arret);

  // bouton Reset : redéfinit tous les paramètres initiaux
  reset_btn = createButton('Reset');
  reset_btn.style('width', '200px');
  reset_btn.parent('widgets');
  reset_btn.mousePressed(raz);

  // widget (associé à un booléen) permettant l'éclairage d'un point de la corde vibrante
  eclairage = createCheckbox('Éclairer un point', false);
  eclairage.parent('eclairage_widget');

 }

function draw(){
  var rayon = 5; // taille des points dessinés
  var nb_pt;
  var pas = 5; // changer ce paramètre pour modifier la densité de points dessinés
  nb_pt = 0.9*width/pas;
  if (!pause){ // on change d'image si l'animation n'est pas en pause
    img += 1;
  }
  t = img/fps; // le temps est lié au numéro de l'image et au frameRate (frame per second)
  background(0);
  var A = amp*height/2;
  if (eclairage.checked()){ // on met en éclairage un point de la corde vibrante
    fill(255);
    rect(0.05*width + 3.5*pas, (height/2-A)-rayon, 5, 2*(A+rayon));
  }
  fill(255,0,0);
  for (var point=0; point<=nb_pt; point++){
    var x = point*pas;
    var y = A * cos(TWO_PI * (t/T - x/lambda)); // calcul de l'amplitudse de l'onde à l'instant t et à la position x
    ellipse(0.05*width + x, height/2 + y, rayon);
  }
  fill(255,0,255);
  textSize(20);
  text('T = '+T_slider.value()+' s'+'   L = '+L_slider.value()+' m'+'   A = '+A_slider.value()+' m', 50, 20);
  fill(255,0,0);
  }

function maj(){
  T = T_slider.value();
  lambda = L_slider.value();
  amp = A_slider.value();
}

function raz(){
  T_slider.value(1);
  L_slider.value(100);
  A_slider.value(0.5);
  maj()
}

function arret(){
  pause = !pause;
}
