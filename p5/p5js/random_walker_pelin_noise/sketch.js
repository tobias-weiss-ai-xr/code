let w; // Walker object
let t; // time object

function setup() {
  createCanvas(800, 600);
  background(51); // gray
  w = new Walker();
  t = 0.0;
}

function draw() {
  t += 0.01;
  w.render();
  w.move(t);
}

// Jitter class
class Walker {
  constructor() {
    this.x = width/2; 
    this.y = height/2;
  }

  move(t) {
    let x = noise(t) * 4
    console.log(x)
    if (x < 1) {
      this.x++;
    } else if (x < 2) {
      this.x--;
    } else if (x < 3) {
      this.y++;
    } else {
      this.y--;
    }

    // do not jump over the border limits
    this.x = constrain(this.x, 0, width-1);
    this.y = constrain(this.y, 0, height-1);
  }

  render() {
    stroke(255)
    point(this.x, this. y)
  }
}