//camera path
var position1 = {x: -9.9, y: 0.5, z: 50};
var _target1 = {x: -9.9, y: 0.5, z: 50};
var tween1 = new TWEEN.Tween(position1).to(_target1, 500);
tween1.onUpdate(function(){ 
	toIntersect[5].interact();
});
tween1.delay(3000);

var position2 = {x: -9.9, y: 0.5, z: 50};
var _target2 = {x: -9.9, y: 0.5, z: 34};
var tween2 = new TWEEN.Tween(position2).to(_target2, 2000);
tween2.onUpdate(function(){ 
  controls.getObject().position.x = position2.x;
  controls.getObject().position.y = position2.y;
  controls.getObject().position.z = position2.z;
});
tween2.delay(1500);

var position3 = camera.rotation;
var _target3 = { y: -Math.PI/2 };
var tween3 = new TWEEN.Tween(position3).to(_target3, 500);
tween3.delay(1000);

var position4 = {x: -9.9, y: 0.5, z: 34};
var _target4 = {x: -9.9, y: 0.5, z: 34};
var tween4 = new TWEEN.Tween(position1).to(_target1, 400);
tween4.onUpdate(function(){ 
	toIntersect[0].interact();
});
tween4.delay(1000);

var position5 = {x: -9.9, y: 0.5, z: 34};
var _target5 = {x: -6, y: 0.5, z: 34};
var tween5 = new TWEEN.Tween(position5).to(_target5, 1500);
tween5.onUpdate(function(){ 
  controls.getObject().position.x = position5.x;
  controls.getObject().position.y = position5.y;
  controls.getObject().position.z = position5.z;
});
tween5.delay(1500);

var position6 = {x: -6, y: 0.5, z: 34};
var _target6 = {x: -3.5, y: 0.5, z: 37};
var tween6 = new TWEEN.Tween(position6).to(_target6, 1500);
tween6.onUpdate(function(){ 
  controls.getObject().position.x = position6.x;
  controls.getObject().position.y = position6.y;
  controls.getObject().position.z = position6.z;
});
tween6.delay(1000);

var position7 = camera.rotation;
var _target7 = { y:2*Math.PI };
var tween7 = new TWEEN.Tween(position7).to(_target7, 20000);
tween7.delay(1000);

var position8 = camera.rotation;
var _target8 = { y:Math.PI/2 };
var tween8 = new TWEEN.Tween(position7).to(_target7, 1500);
tween8.delay(1000);

var position9 = {x: -3.5, y: 0.5, z: 37};
var _target9 = {x: -3.5, y: 0.5, z: 28};
var tween9 = new TWEEN.Tween(position9).to(_target9, 1500);
tween9.onUpdate(function(){ 
  controls.getObject().position.x = position9.x;
  controls.getObject().position.y = position9.y;
  controls.getObject().position.z = position9.z;
});
tween9.delay(1000);

var position11 = {x: -3.5, y: 0.5, z: 28};
var _target11 = {x: -3.5, y: 0.5, z: 34};
var tween11 = new TWEEN.Tween(position11).to(_target11, 1500);
tween11.onUpdate(function(){ 
  controls.getObject().position.x = position11.x;
  controls.getObject().position.y = position11.y;
  controls.getObject().position.z = position11.z;
});
tween11.delay(17000);

var position12 = {x: -3.5, y: 0.5, z: 34};
var _target12 = {x: -10, y: 0.5, z: 34};
var tween12 = new TWEEN.Tween(position12).to(_target12, 1000);
tween12.onUpdate(function(){ 
  controls.getObject().position.x = position12.x;
  controls.getObject().position.y = position12.y;
  controls.getObject().position.z = position12.z;
});
tween12.delay(1000);

var position13 = {x: -10, y: 0.5, z: 34};
var _target13 = {x: -10, y: 0.5, z: 22};
var tween13 = new TWEEN.Tween(position13).to(_target13, 1000);
tween13.onUpdate(function(){ 
  controls.getObject().position.x = position13.x;
  controls.getObject().position.y = position13.y;
  controls.getObject().position.z = position13.z;
});
tween13.delay(1000);

var position14 = {x: -10, y: 0.5, z: 22};
var _target14 = {x: -16, y: 0.5, z: 13};
var tween14 = new TWEEN.Tween(position14).to(_target14, 1500);
tween14.onUpdate(function(){ 
  controls.getObject().position.x = position14.x;
  controls.getObject().position.y = position14.y;
  controls.getObject().position.z = position14.z;
});
tween14.delay(1000);

var position15 = camera.rotation;
var _target15 = { y:Math.PI };
var tween15 = new TWEEN.Tween(position15).to(_target15, 5000);
tween15.delay(1000);

var position17 = {x: -16, y: 0.5, z: 13};
var _target17 = {x: -10, y: 0.5, z: 22};
var tween17 = new TWEEN.Tween(position17).to(_target17, 1500);
tween17.onUpdate(function(){ 
  controls.getObject().position.x = position17.x;
  controls.getObject().position.y = position17.y;
  controls.getObject().position.z = position17.z;
});
tween17.delay(1000);

var position18 = camera.rotation;
var _target18 = { y:-Math.PI/2 };
var tween18 = new TWEEN.Tween(position18).to(_target18, 2000);
tween18.delay(1000);

var position19 = {x: -10, y: 0.5, z: 22};
var _target19 = {x: -8, y: 0.5, z: 22};
var tween19 = new TWEEN.Tween(position19).to(_target19, 1500);
tween19.onUpdate(function(){ 
  controls.getObject().position.x = position19.x;
  controls.getObject().position.y = position19.y;
  controls.getObject().position.z = position19.z;
});

var position20 = {x: -8, y: 0.5, z: 22};
var _target20 = {x: -8, y: 0.5, z: 19};
var tween20 = new TWEEN.Tween(position20).to(_target20, 1500);
tween20.onUpdate(function(){ 
  controls.getObject().position.x = position20.x;
  controls.getObject().position.y = position20.y;
  controls.getObject().position.z = position20.z;
});

var position21 = {x: -8, y: 0.5, z: 19};
var _target21 = {x: -8, y: 0.5, z: 19};
var tween21 = new TWEEN.Tween(position21).to(_target21, 600);
tween21.onUpdate(function(){ 
	toIntersect[1].interact();
});

var position22 = {x: -8, y: 0.5, z: 19};
var _target22 = {x: -6, y: 0.5, z: 19};
var tween22 = new TWEEN.Tween(position22).to(_target22, 1000);
tween22.onUpdate(function(){ 
  controls.getObject().position.x = position22.x;
  controls.getObject().position.y = position22.y;
  controls.getObject().position.z = position22.z;
});
tween22.delay(1000);

var positionR = body.trunk.rotation;
var _targetR = { y:Math.PI/2 };
var tweenR = new TWEEN.Tween(positionR).to(_targetR, 500);

var positionR2 = arm_dx.rotation
var _targetR2 = {y: -1};
var tweenR2 = new TWEEN.Tween(positionR2).to(_targetR2, 500);


var position23 = {x: -6, y: 0.5, z: 19};
var _target23 = {x: -8.5, y: 0.5, z: 19};
var tween23 = new TWEEN.Tween(position23).to(_target23, 1000);
tween23.onUpdate(function(){ 
  controls.getObject().position.x = position23.x;
  controls.getObject().position.y = position23.y;
  controls.getObject().position.z = position23.z;
});
tween23.delay(1000);

var position24 = {x: -8.5, y: 0.5, z: 19};
var _target24 = {x: -8.5, y: 0.5, z: 9.6};
var tween24 = new TWEEN.Tween(position24).to(_target24, 1000);
tween24.onUpdate(function(){ 
  controls.getObject().position.x = position24.x;
  controls.getObject().position.y = position24.y;
  controls.getObject().position.z = position24.z;
});
tween24.delay(1000);

var tween25 = new TWEEN.Tween(_target24).to(_target24, 500);
tween25.onUpdate(function(){ 
  toIntersect[2].interact();
});
tween25.delay(1000);

var position26 = {x: -8.5, y: 0.5, z: 9.6};
var _target26 = {x: -3.6, y: 0.5, z: 9.6};
var tween26 = new TWEEN.Tween(position26).to(_target26, 1000);
tween26.onUpdate(function(){ 
  controls.getObject().position.x = position26.x;
  controls.getObject().position.y = position26.y;
  controls.getObject().position.z = position26.z;
});
tween26.delay(1000);

var position27 = camera.rotation
var _target27 = { y: -Math.PI};
var tween27 = new TWEEN.Tween(position27).to(_target27, 500);


tween1.chain(tween2);
tween2.chain(tween3);
tween3.chain(tween4);
tween4.chain(tween5);
tween5.chain(tween6);
tween6.chain(tween7);
tween7.chain(tween8);
tween8.chain(tween9);
tween9.chain(tween11);
tween11.chain(tween12);
tween12.chain(tween13);
tween13.chain(tween14);
tween14.chain(tween15);
tween15.chain(tween17);
tween17.chain(tween18);
tween18.chain(tween19);
tween19.chain(tween20);
tween20.chain(tween21);
tween21.chain(tween22);
tween22.chain(tweenR);
tweenR.chain(tweenR2);
tweenR2.chain(tween23);
tween23.chain(tween24);
tween24.chain(tween25);
tween25.chain(tween26);
tween26.chain(tween27);

  
var isTour = false;

var make_a_tour = function() {
	if(!isTour)
	{
		enableFirst_Person_Camera();
		tween1.start();
		isTour = true;
	}
	else
	{
		isTour = false;
	}
}
//robot camera
var isON = false;
var RobotCam = function() {
  if(!isON){
    camera.position.set(-2.5,2,21.5);
    isON = true;
  }
  else
  {
    camera.position.set(0,7,50);
    isON = false;
  }
}
//controls
var controls = new function() {
    this.enableTrackball = true;
    this.enableFirst_Person_Camera = enableFirst_Person_Camera;
    this.make_a_tour = make_a_tour;
    this.Turn_On_Lights = Turn_On_Lights;
    this.Day_or_Night = Day_or_Night;
    this.RobotCam = RobotCam;
    //robot

	  //body
	  this.X = 0.0;
	  this.Y = 0.0;
	  this.Z = 0.0;

	  //right arm
	  this.arm_dx = 0.0;
	  this.shoulder_dx = 0.0;
	  this.forearm_dx = 0.0;
	  this.hand_dx = 0.0;
	  this.fingerA_dx = 0.0;
	  this.fingerA_flexor_dx = 0.0;
	  this.fingerB_dx = 0.9;
	  this.fingerB_flexor_dx = 0.7;
	  
	  //left arm
	  this.arm_sx = 0.0;
	  this.shoulder_sx = 0.0;
	  this.forearm_sx = 0.0;
	  this.hand_sx = 0.0;
	  this.fingerA_sx = 0.0;
	  this.fingerA_flexor_sx = 0.0;
	  this.fingerB_sx = 0.9;
	  this.fingerB_flexor_sx = 0.7;

	  //right leg
	  this.leg_dx = 0.0;
	  this.hip_dx = 0.0;
	  this.tibia_dx = 0.0;
	  this.knee_dx = 0.0;
	  this.foot_dx = 0.0;
	  this.ankle_dx = 0.0;
	  
	  //left leg
	  this.leg_sx = 0.0;
	  this.hip_sx = 0.0;
	  this.tibia_sx = 0.0;
	  this.knee_sx = 0.0;
	  this.foot_sx = 0.0;
	  this.ankle_sx = 0.0;

	//
};

var gui = new dat.GUI();

//body
var bodyContent = gui.addFolder('Body');
bodyContent.add(controls, 'Y', -2/3*Math.PI, 2/5*Math.PI).onChange(function (value) {
  body.trunk.rotation.y = value; 
});
bodyContent.add(controls, 'X', -Math.PI/12, -Math.PI/12).onChange(function (value) {
  body.trunk.rotation.x = value; 
});
bodyContent.add(controls, 'Z', -Math.PI/12, Math.PI/12).onChange(function (value) {
  body.trunk.rotation.z = value; 
});

//right arm
var arm_r = gui.addFolder('Right Arm');
arm_r.add(controls, 'arm_dx', -2/3*Math.PI, 2/5*Math.PI).onChange(function (value) {
  arm_dx.rotation.y = value; 
});
arm_r.add(controls, 'shoulder_dx', -2/3*Math.PI, 1/3*Math.PI).onChange(function (value) {
  arm_dx.sphere.rotation.z = value; 
});

arm_r.add(controls, 'forearm_dx', 0.0, 2*Math.PI).onChange(function (value) {
  arm_dx.avambraccio.rotation.y = value; 
});
arm_r.add(controls, 'hand_dx', 0.0, Math.PI/2).onChange(function (value) {
  arm_dx.avambraccio.sphere.rotation.x = value; 
});

arm_r.add(controls, 'fingerA_dx', 0.0, Math.PI*2).onChange(function (value) {
  arm_dx.dito0.rotation.y = value; 
});
arm_r.add(controls, 'fingerA_flexor_dx', 0.0, Math.PI/2).onChange(function (value) {
  arm_dx.dito0.sphere.rotation.x = value; 
});

arm_r.add(controls, 'fingerB_dx', 0.0, 2*Math.PI).onChange(function (value) {
  arm_dx.dito1.rotation.y = value; 
});
arm_r.add(controls, 'fingerB_flexor_dx', 0.0, Math.PI/2).onChange(function (value) {
  arm_dx.dito1.sphere.rotation.x = value; 
});

//left arm
var arm_r = gui.addFolder('Left Arm');
arm_r.add(controls, 'arm_sx', -2/3*Math.PI, 2/5*Math.PI).onChange(function (value) {
  arm_sx.rotation.y = value; 
});
arm_r.add(controls, 'shoulder_sx', -2/3*Math.PI, 1/3*Math.PI).onChange(function (value) {
  arm_sx.sphere.rotation.z = value; 
});

arm_r.add(controls, 'forearm_sx', 0.0, 2*Math.PI).onChange(function (value) {
  arm_sx.avambraccio.rotation.y = value; 
});
arm_r.add(controls, 'hand_sx', 0.0, Math.PI/2).onChange(function (value) {
  arm_sx.avambraccio.sphere.rotation.x = value; 
});

arm_r.add(controls, 'fingerA_sx', 0.0, Math.PI*2).onChange(function (value) {
  arm_sx.dito0.rotation.y = value; 
});
arm_r.add(controls, 'fingerA_flexor_sx', 0.0, Math.PI/2).onChange(function (value) {
  arm_sx.dito0.sphere.rotation.x = value; 
});

arm_r.add(controls, 'fingerB_sx', 0.0, 2*Math.PI).onChange(function (value) {
  arm_sx.dito1.rotation.y = value; 
});
arm_r.add(controls, 'fingerB_flexor_sx', 0.0, Math.PI/2).onChange(function (value) {
  arm_sx.dito1.sphere.rotation.x = value; 
});

//right leg
var leg_r = gui.addFolder('Right Leg');
leg_r.add(controls, 'leg_dx', -2/3*Math.PI, 2/5*Math.PI).onChange(function (value) {
  leg_dx.rotation.y = value; 
});
leg_r.add(controls, 'hip_dx', -2/3*Math.PI, 1/3*Math.PI).onChange(function (value) {
  leg_dx.sphere.rotation.z = value; 
});

leg_r.add(controls, 'tibia_dx', 0.0, 2*Math.PI).onChange(function (value) {
  leg_dx.tibia.rotation.y = value; 
});
leg_r.add(controls, 'knee_dx', 0.0, Math.PI/2).onChange(function (value) {
  leg_dx.tibia.sphere.rotation.x = value; 
});

leg_r.add(controls, 'foot_dx', 0.0, Math.PI*2).onChange(function (value) {
  leg_dx.piede.rotation.y = value; 
});
leg_r.add(controls, 'ankle_dx', 0.0, Math.PI/2).onChange(function (value) {
  leg_dx.piede.sphere.rotation.x = value; 
});

//left leg
var leg_l = gui.addFolder('Left Leg');
leg_l.add(controls, 'leg_sx', -2/3*Math.PI, 2/5*Math.PI).onChange(function (value) {
  leg_sx.rotation.y = value; 
});
leg_l.add(controls, 'hip_sx', -2/3*Math.PI, 1/3*Math.PI).onChange(function (value) {
  leg_sx.sphere.rotation.z = value; 
});

leg_l.add(controls, 'tibia_sx', 0.0, 2*Math.PI).onChange(function (value) {
  leg_sx.tibia.rotation.y = value; 
});
leg_l.add(controls, 'knee_sx', 0.0, Math.PI/2).onChange(function (value) {
  leg_sx.tibia.sphere.rotation.x = value; 
});

leg_l.add(controls, 'foot_sx', 0.0, Math.PI*2).onChange(function (value) {
  leg_sx.piede.rotation.y = value; 
});
leg_l.add(controls, 'ankle_sx', 0.0, Math.PI/2).onChange(function (value) {
  leg_sx.piede.sphere.rotation.x = value; 
});

var cameraF = gui.addFolder('Camera');
cameraF.add(controls, "enableTrackball");

cameraF.add(controls, "enableFirst_Person_Camera");

var time = gui.addFolder('Time');
time.add(controls, "Turn_On_Lights");

time.add(controls, "Day_or_Night");

var rob = gui.addFolder('RobotCamera');
rob.add(controls, "RobotCam");

var tour = gui.addFolder('Tour (beta)');
tour.add(controls, "make_a_tour");

var sky = mkDAYskybox();
scene.add(sky);