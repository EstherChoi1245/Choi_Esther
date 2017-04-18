function text()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	

	window.addEventListener("mousemove", icon, false);

}

function icon(e) {
	var pic = new Image();
	pic.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/SNice.svg/1200px-SNice.svg.png";
	pic.addEventListener("load", text, false);
	
	canvas.clearRect(0, 0, 600, 600);
	var xPos = e.clientX; 
	var yPos = e.clientY;
	canvas.fillRect(canvas.drawImage(pic, xPos, yPos, 200, 200));

	
}

window.addEventListener("mousemove", text, false);

