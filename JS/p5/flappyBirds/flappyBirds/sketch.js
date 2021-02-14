var bird;
var pipes = [];
function setup()
 {
	//createCanvas(windowWidth, windowHeight);
	width = windowWidth;
	height = windowHeight;
  createCanvas(width,height);
	bird = new Bird();
	pipes.push(new Pipe());
}

function draw() {
	background(0);

	// show pipes
	for(var i = pipes.length-1; i >= 0; i--){
		pipes[i].show();
		pipes[i].update();

		// check if the bird hits
		if (pipes[i].hits(bird)) {
			console.log("HIT!");
		}

		// remove pipe from array if it is
		// not visible any more
		if (pipes[i].offscreen()) {
			pipes.splice(i,1);
		}
	}



	bird.show();
  bird.update();

	if (frameCount % 80 == 0) {
			pipes.push(new Pipe());
	}


}

function keyPressed() {
	if (key == ' ') {
		//console.log("SPACE");
		bird.up();
	}
}
