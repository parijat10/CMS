colorList = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'aquamarine', 'brown', 'silver'];
noOfBots = 9;
function main() {
    canvas = document.getElementById("controlCan");
    $('#controlDiv').show();
    $('#selectDiv').hide();
    $('#commandBot').html("End Control");
    $('#commandBot').click(function() {
    	$('#controlDiv').hide();
    	$('#selectDiv').show();
    	$('#commandBot').html('Take Control');
    	$('#commandBot').click(main);
        $('.arrow').off();
    });
    $('.arrow').click(function(e) {
            moveRobot(e);
    });
    con = canvas.getContext("2d");
    con.drawImage(document.getElementById("mapImg"), 0, 0, canvas.width, canvas.height);
    con.strokeRect(0,0,canvas.width, canvas.height);
}

function moveRobot(e) {
    $.ajax({
        url: '/command/moveBot', 
        data: {'dir': e.target.id}, 
        success: function(r) {
            console.log('Move call over!', r);
        }
    });
}
