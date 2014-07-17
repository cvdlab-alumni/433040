//pc tween
var openPCTween;
var closePCTween;

function importPCAnimations(pc) {
	openPCTween = new TWEEN.Tween(pc.parent.rotation)
		.to({
			x: -2
		}, 1000)
		.easing(TWEEN.Easing.Cubic.Out);
	closePCTween = new TWEEN.Tween(pc.parent.rotation)
		.to({
			x: 0
		}, 1000)
		.easing(TWEEN.Easing.Cubic.Out);
}

//Doors tween
var doorHandleOpenTween;
var doorOpenTween;
var doorCloseTween;

function applyDoorAnimations(door, opening) {
	doorHandleOpenTween = new TWEEN.Tween(door.children[2].rotation)
		.to({
			y: -0.5,
		}, 500)
		.easing(TWEEN.Easing.Cubic.Out)
		.repeat(1)
		.yoyo(true);
	doorOpenTween = new TWEEN.Tween(door.parent.rotation)
		.to({
			z: -1* Math.PI / 2,
		}, 1000)
		.easing(TWEEN.Easing.Cubic.Out)
		.delay(200);
	doorCloseTween = new TWEEN.Tween(door.parent.rotation)
		.to({
			z: 0,
		}, 1000)
		.easing(TWEEN.Easing.Cubic.Out);
}

//Lights tween
var lampLight1OffTween;
var lampLight2OffTween;
var lampLight1OnTween;
var lampLight2OnTween;

function applyLightAnimations(lamp) {
	lampLight1OffTween = new TWEEN.Tween(lamp.children[0].children[2])
		.to({
			intensity: 0
		}, 300);
	lampLight2OffTween = new TWEEN.Tween(lamp.children[0].children[3])
		.to({
			intensity: 0
		}, 300);
	lampLight1OnTween = new TWEEN.Tween(lamp.children[0].children[2])
		.to({
			intensity: 2
		}, 1000)
		.easing(TWEEN.Easing.Bounce.In);
	lampLight2OnTween = new TWEEN.Tween(lamp.children[0].children[3])
		.to({
			intensity: 5
		}, 1000)
		.easing(TWEEN.Easing.Bounce.In);
}