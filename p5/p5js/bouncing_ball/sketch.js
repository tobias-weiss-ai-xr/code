PVector loc;
PVector v;

function setup(){
  createCanvas(400, 400);
  loc = new PVector(100, 100)
  v = new PVector(2.5, 5)
}

function draw(){
  background(255);
  location.add(velocity)

  if ((location.x > width) || (location.x < 0)) {
    velocity.x = velocity.x * -1;
  }
  if ((location.y > height) || (location.y < 0)) {
    velocity.y = velocity.y * -1;
  }
  stroke(0);
  fill(175);
  ellipse(location.x,location.y,16,16);
}
