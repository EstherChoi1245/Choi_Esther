function shapes()	{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");	
	// canvas.addColorStop(0, "blue");
	// canvas.addColorStop(.5, "white");
	// canvas.addColorStop(1, "red");	
	canvas.strokeStyle = "yellow";
	canvas.fillStyle = "red";
	canvas.beginPath();

	canvas.moveTo(780, 1070);
	canvas.lineTo(895, 1400); 
	canvas.lineTo(1010, 1080);
	canvas.lineTo(1340, 1270); 
	canvas.lineTo(1170, 920);
	canvas.lineTo(1550, 820); 
	canvas.lineTo(1180, 690);
	canvas.lineTo(1390, 382); 
	canvas.lineTo(1020, 530);
	canvas.lineTo(905, 200); 
	canvas.lineTo(790, 520);
	canvas.lineTo(500, 380);
	canvas.lineTo(630, 680);
	canvas.lineTo(330, 795); 
	canvas.lineTo(620, 910);
	canvas.lineTo(450, 1225); 


	canvas.closePath();
	canvas.stroke();
	canvas.fill();
	
	}

window.addEventListener("load", shapes, false);
