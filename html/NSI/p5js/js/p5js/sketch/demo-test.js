function setup() {

  var canvas1 = createCanvas(1600, 800, WEBGL); // 1ère ligne obligatoire !
  canvas1.parent('sketch1');
  /* dispose le canvas dans le div avec id='sketch1'
  sinon, par défaut le sketch est en fin de doc html */

  describe(
    "teste le contrôle orbital"
  );

}

function draw() {
  background(250);
  let radius = width * 1.5;

  //drag to move the world.
  orbitControl();

 normalMaterial();
  //
  sphere(100);
  //cone(50, 70);
  torus(50, 20);
}

