window.addEventListener("load", main);
colorList = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'aquamarine', 'brown', 'silver'];
noOfBots = 9;
intervalTime = 1;
xyCoord = [];
coordinates = [0, 0];

function main() {
    canvas = document.getElementById("mapCan");
    con = canvas.getContext("2d");
    con.drawImage(document.getElementById("mapImg"), 0, 0, canvas.width, canvas.height);
    keyDiv = document.getElementById('key');
    for (var i = 0; i < noOfBots; i++) {
        (function(i){
            setInterval(function(){drawRobot(colorList[i], i);}, intervalTime*1000);
            var keyElem = document.createElement('div');
            keyElem.className = "colorDot";
            keyElem.style.backgroundColor = colorList[i];
            var keySpan = document.createElement('span');
            keySpan.innerHTML = "Robot "+(i+1);
            keySpan.className = "robotNumber";
            keyDiv.appendChild(keyElem);
            keyDiv.appendChild(keySpan);
        })(i);
    };
    selectTag = document.getElementById('robotList');
    for (var i = 0; i<noOfBots; i++){
        var opt = document.createElement('option');
        opt.innerHTML = "Robot "+(i+1);
        opt.value = (i+1);
        selectTag.appendChild(opt);
    }
    $('#checkStatus').click(
            function() {
                index = $('#robotList').find(':selected').val()-1;
                $('#statusDisplay').html(
                    "<h3 id=\"heading\">Status of Robot "+(index+1)+"</h3><h4>x: "+xyCoord[index][0]+"<br>y: "+xyCoord[index][1]+"</h4>"
                    );
            }
    );
    window.addEventListener('mousemove', mouse_position);
}

function drawRobot(color, index)
{
    x = coordinates[0];
    y = coordinates[1];
    console.log(x, y);
    if(color==colorList[0]) con.drawImage(document.getElementById("mapImg"), 0, 0, canvas.width, canvas.height);
    con.beginPath();
    con.fillStyle=color;
    con.arc(x, y, 8, 0, 2*Math.PI);
    con.fill();
    xyCoord[index] = [x, y];
}

function mouse_position(e)
{
	$.ajax({url: '/status/read_coordinates', success: function(r) {
        r.split(', ');
        coordinates[0] += (parseInt(r.split(', ')[3].split(': ')[1])*canvas.width/window.innerWidth);
        coordinates[1] -= (parseInt(r.split(', ')[4].split(': ')[1])*canvas.height/window.innerHeight);
      }
    });
	drawRobot('red', 0);
}
