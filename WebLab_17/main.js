function drag() {
	coffee = document.getElementById("coffee");
	leftbox = document.getElementById("leftBox");
	
	coffee.addEventListener("dragstart", startDrag, false);
	coffee.addEventListener("dragend", endDrag, false);
	
	leftbox.addEventListener("dragenter", dragEnter, false);
	leftbox.addEventListener("dragleave", dragLeave, false);
	leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftbox.addEventListener("drop", drop, false);
	
}

function startDrag(e) {
	var pic = '<img id = "coffee" src = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/A_small_cup_of_coffee.JPG/1024px-A_small_cup_of_coffee.JPG">';
	e.dataTransfer.setData('Picture', pic);
	
}

function dragEnter(e) {
	e.preventDefault();
	leftbox.style.background = "pink"; 
	leftbox.style.border = "3px solid gray";
	
}

function dragLeave(e) {
	e.preventDefault();
	leftbox.style.background = "red"; 
	leftbox.style.border = "3px solid orange";
	
}

function drop(e) {
	e.preventDefault();
	leftBox.innerHTML = e.dataTransfer.getData('Picture');
	
}

function endDrag(e) {
	pic = e.target
	pic.style.visibility = "hidden";
}

window.addEventListener("load", drag, false);


