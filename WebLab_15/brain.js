function shapes()	{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	canvas.strokeStyle = "yellow";
	canvas.fillStyle = "purple";
	canvas.beginPath();
	canvas.moveTo(50, 50);
	canvas.lineTo(100,100);
	canvas.lineTo(300, 200);
	canvas.closePath();
	canvas.stroke();
	canvas.fill();
	
	
	// var g = canvas.createLinearGradient(10, 10, 100, 200);
	// g.addColorStop(0, "blue");
	// g.addColorStop(.5, "white");
	// g.addColorStop(1, "red");	
	// canvas.fillStyle = g;
	// canvas.fillRect(10, 10, 100, 200);
	}

window.addEventListener("load", shapes, false);
