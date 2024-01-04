let myShader;

function preload() {
  // load each shader file (don't worry, we will come back to these!)
  myShader = loadShader('shaders/shader1.vert', 'shaders/shader1.frag');
}

function setup() {
  // the canvas has to be created with WEBGL mode

  var canvas1 = createCanvas(700, 400, WEBGL); // 1ère ligne obligatoire !
  canvas1.parent('sketch1');
  /* dispose le canvas dans le div avec id='sketch1'
  sinon, par défaut le sketch est en fin de doc html */
 
  describe('a simple shader example that outputs the color red')
}

function draw() {
  // shader() sets the active shader, which will be applied to what is drawn next
  shader(myShader);
  // apply the shader to a rectangle taking up the full canvas
  rect(0, 0, 80, 20);
}