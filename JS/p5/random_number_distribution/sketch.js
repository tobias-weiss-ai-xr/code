let random_counts;

function setup() {
  createCanvas(800, 400);
  background(51); // gray
  random_counts = new Array(20).fill(0);
}

function draw() {
  background(255);

  let idx = int(random(random_counts.length));
  random_counts[idx]++;

  stroke(0);
  fill(175);
  let w = width/random_counts.length;
  for (let x = 0; x < random_counts.length; x++) {
    rect(x*w, height-random_counts[x], w-1, random_counts[x])
    
  }
}
