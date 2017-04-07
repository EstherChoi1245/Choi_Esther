function shapes()	{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");	
	

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
	canvas.lineTo(450, 370);
	canvas.lineTo(630, 680);
	canvas.lineTo(310, 795); 
	canvas.lineTo(620, 910);
	canvas.lineTo(450, 1225); 
	canvas.closePath();

	
	var g = canvas.createLinearGradient(20, 20, 2000, 2000);
	g.addColorStop(0, "#DF00FF");
	g.addColorStop(.2, "#DA70D6");	
	g.addColorStop(.4, "#DCDCDC");
	//g.addColorStop(.45, "gray");
	g.addColorStop(0.85, "#FDFF00");
	g.addColorStop(0.9, "#FFFF00");

	canvas.fillStyle = g;	
	canvas.fill();
	

	
	}

window.addEventListener("load", shapes, false);
