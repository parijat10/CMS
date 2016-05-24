var localMediaStream = null;
var video;

window.addEventListener('load', main)

var errorCallback = function(e) {
    console.log(e);
};

var hdConstraints = {
  video: {
    mandatory: {
      minWidth: 1280,
      minHeight: 720
    }
  },
  audio: true
};

var vgaConstraints = {
  video: {
    mandatory: {
      maxWidth: 640,
      maxHeight: 360
    }
  }
};

var screenConstraints = {
	video: {
		mandatory: {chromeMediaSource: 'screen'}
	},
	audio: true
};

function main()
{
	navigator.getUserMedia  = navigator.getUserMedia ||
                      navigator.webkitGetUserMedia ||
                      navigator.mozGetUserMedia ||
                      navigator.msGetUserMedia;
	video = document.querySelector('video');
	if (navigator.getUserMedia) {
		navigator.getUserMedia(hdConstraints, function(stream) {
		console.log(stream);
		window.stream = stream;
		if(window.URL)
		{
			video.src = window.URL.createObjectURL(stream);
		}
		else{
			video.src = stream;
		}
	 	localMediaStream = stream;
		}, errorCallback);
	} else {
	  alert(1);
	}
}
