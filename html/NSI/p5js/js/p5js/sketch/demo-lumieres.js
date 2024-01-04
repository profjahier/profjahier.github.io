function setup() {
  


  var canvas1 = createCanvas(710, 400, WEBGL); // 1ère ligne obligatoire !
  canvas1.parent('sketch1');
  /* dispose le canvas dans le div avec id='sketch1'
  sinon, par défaut le sketch est en fin de doc html */

  describe(
    'a 3d example containing seven primitive objects, a plane, box, cylinder, cone, torus, sphere, and ellipsoid.'
  );
  
}

function draw() {
  background(0);

  let locX = mouseX - height / 2;
  let locY = mouseY - width / 2;

  // ambient light is gray
ambientLight(50);
  // directional light is red
directionalLight(255, 0, 0, 0.25, 0.25, 0);
  // spotlight is green
  spotLight(0, 255, 0, 150, 0, 250, 0, 0, -1);
  // point light is blue
  pointLight(0, 0, 255, locX, locY, 250);

  push();
  translate(-width / 4, 0, 0);
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  specularMaterial(250);
  box(100, 100, 100);
  pop();

  translate(width / 4, 0, 0);
  ambientMaterial(250);
  sphere(120, 24);
}
