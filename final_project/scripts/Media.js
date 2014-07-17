var soundsToUpdate = []

var Sound = function(src, radius, volume, toUpdate, loop) {
	var audio = document.createElement('audio');
	var source = document.createElement('source');
	source.src = 'assets/sounds/' + src;
	audio.appendChild(source);
	this.position = new THREE.Vector3();
	audio.volume = volume;
	audio.loop = loop;
	this.play = function() {
		audio.play();
	}
	this.pause = function() {
		audio.pause();
	}
	this.stop = function() {
		audio.pause();
		audio.currentTime = 0;
	}
	this.updateVolume = function() {
		var distance = this.position.distanceTo((!FPenabled) ? camera.position : controls.getObject().position);
		if (distance <= radius) {
			audio.volume = volume * (1 - distance / radius);
		} else {
			audio.volume = 0;
		}
	}
	if (toUpdate) {
		soundsToUpdate.push(this);
	}
}

var door_open_sound = new Sound(['door_open.mp3'], 0, 0.1, false);
var door_close_sound = new Sound(['door_close.mp3'], 0, 0.1, false);