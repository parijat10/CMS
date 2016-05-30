window.addEventListener("load", main);
intervalTime = 1;
xyCoord = [];
coordinates = [0, 0];

function main() {
    canvas = document.getElementById("mapCan");
    con = canvas.getContext("2d");
    con.drawImage(document.getElementById("mapImg"), 0, 0, canvas.width, canvas.height);
    canvas.addEventListener("click", function(e) {
	    getCoordinates(e);
    });
    $('#commandBot').click(function() { 
    	sendCommand();
    });
}

function getCoordinates(e) {
	var rect = canvas.getBoundingClientRect();
	coordinates = [Math.round(e.clientX - rect.left, 0), Math.round(e.clientY - rect.top, 0)];
	$('#xycoords').html("x: "+coordinates[0]+"<br />"+"y: "+coordinates[1]);
}

function sendCommand() {
	$.ajax({
		url: "/command/sendCoord",
		data: {'xcoord': coordinates[0], 'ycoord': coordinates[1]},
		success: function(r) {
			console.log("Coordinates sent!", r);
		}
	});
}
