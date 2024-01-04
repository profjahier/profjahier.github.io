function setup(){
  var canvas1 = createCanvas(400, 150); // 1ère ligne obligatoire !
  canvas1.parent('sketch1');
  /* dispose le canvas dans le div avec id='sketch1'
  sinon, par défaut le sketch est en fin de doc html */
  frameRate(2);
  print('Deux images par seconde : frameRate(2);'); //  affichage en console
  background(0);
}

function draw(){
  print("Image n°"+ frameCount);
}
