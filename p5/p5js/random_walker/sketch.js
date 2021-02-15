let w; // Declare walker

function setup() {
  createCanvas(800, 600);
  // Create object
  background(51);
  w = new Walker();
}

function draw() {
  w.render();
  w.move();
}

// Jitter class
class Walker {
  constructor() {
    this.x = width/2; 
    this.y = height/2;
  }

  move() {
    let rnd = int(random(4));
    if (rnd == 3) {
      this.x++;
    } else if (rnd == 2) {
      this.x--;
    } else if (rnd == 1) {
      this.y++;
    } else {
      this.y--;
    }
    this.x = constrain(this.x, 0, width-1);
    this.y = constrain(this.y, 0, height-1);
  }

  render() {
    stroke(255)
    point(this.x, this. y)
  }
}