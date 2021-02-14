
var angle = 0;
var length = 80;
var slider;

function setup() {
  createCanvas(400, 400);
  slider = createSlider(0,TWO_PI,PI / 4, 0.1);
}

function draw() {
  background(51);
  angel = slider.value();
  stroke(255);
  translate(200, height);
  branch(length);
}

function branch(len){
  line(0, 0, 0, -len);
  translate(0, -len);
  if (len > 9) {
    push();
    rotate(angel);
    branch(len*3/4);
    pop();
    push();
    rotate(-angel);
    branch(len*3/4);
    pop();
  }
}
