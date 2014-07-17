var ambientLight = [];
// day light
DAY_Light = new THREE.HemisphereLight('#C6F1ED', '#ffffff', 0.5);
DAY_Light.position.set(0, 10, 0);
scene.add(DAY_Light);
ambientLight.push(DAY_Light);

isDay = true;

var Day_or_Night = function() {
	if(isDay)
	{
		ambientLight[0].intensity = 0;
		changeSky(false);
		Turn_On_Lights();
		isDay = false;
	}
	else
	{
		ambientLight[0].intensity = 0.3;
		changeSky(true);
		Turn_On_Lights();
		isDay = true;
	}
}

function changeSky(isTimeToDay){
	if(isTimeToDay)
	{
		var selectedObject = scene.getObjectByName("sky");
    	scene.remove( selectedObject );
    	var day = mkDAYskybox();
    	scene.add(day);
	}
	else
	{
		var selectedObject = scene.getObjectByName("sky");
    	scene.remove( selectedObject );
    	var night = mkNIGHTskybox();
    	scene.add(night);
	}
}

var lights = [];

function mkLamp() {
	var lamp = new THREE.Object3D();
	lamp.scale.set(0.2, 0.1, 0.2);
	lamp.rotation.x = -Math.PI / 2;
	// lamp
	var lamp_Geom = new THREE.SphereGeometry(2, 16, 16, 0, 2 * Math.PI, 0, Math.PI / 2);
	var lamp_ext = new THREE.Mesh(lamp_Geom, new THREE.MeshPhongMaterial({ color: '#4E4E4E', shininess: 200, metal: true}));
	var lamp_int = new THREE.Mesh(lamp_Geom,  new THREE.MeshPhongMaterial({
		color: '#aaaaff', 
		shading: THREE.FlatShading, 
		side: THREE.BackSide, 
		shininess: 300, 
		specular: '#ffffff', 
		metal: true
	}));

	lamp_int.scale.set(0.95, 0.95, 0.95);
	var lampshade = new THREE.Object3D();
	lampshade.add(lamp_ext);
	lampshade.add(lamp_int);
	lampshade.rotation.x = Math.PI;
	lamp.add(lampshade);
	// lamp closure
	var closure_Geom = new THREE.TorusGeometry(2, 0.1, 16, 16);
	var closure = new THREE.Mesh(closure_Geom, new THREE.MeshPhongMaterial({ color: '#4E4E4E', shininess: 200, metal: true}));
	closure.rotation.x = Math.PI / 2;
	lamp.add(closure);
	// bulb
	var bulb_Geom = new THREE.SphereGeometry(0.7, 16, 16);
	var bulb = new THREE.Mesh(bulb_Geom, new THREE.MeshPhongMaterial({
		color: '#CEF6F5',
		opacity: 0.6,
		transparent: true,
		shininess: 300,
		specular: '#ffffff',
		metal: true
	}));

	bulb.position.y = -1;
	lamp.add(bulb);
	// glass
	var glass_G = new THREE.CylinderGeometry(2, 1.9, 0.2, 10, 10);
	var glass = new THREE.Mesh(glass_G, new THREE.MeshPhongMaterial({
		color: '#CEF6F5',
		opacity: 0.6,
		transparent: true,
		shininess: 300,
		specular: '#ffffff',
		metal: true
	}));
	glass.position.y = -0.05;
	lamp.add(glass);
	//add lights
	var Light = new THREE.SpotLight('#E1F8F8');
	Light.target = glass;
	Light.angle = Math.PI / 2;
	Light.exponent = 1;
	Light.intensity = 0;
	Light.distance = 10;
	lampshade.add(Light);

	var Light_bulb = new THREE.PointLight('#E1F8F8');
	Light_bulb.position = bulb.position;
	Light_bulb.position.y += 0.1;
	Light_bulb.distance = 0.4;
	Light_bulb.intensity = 0;
	lampshade.add(Light_bulb);
	lamp.rotation.x = Math.PI;

	// add interact function
	lamp.isOn = false;
	lamp.interact = function() {
		applyLightAnimations(this);
		if (this.isOn) {
			lampLight1OffTween.start();
			lampLight2OffTween.start();
			this.isOn = false;
		} else {
			lampLight1OnTween.start();
			lampLight2OnTween.start();
			this.isOn = true;
		}
	}
	lights.push(lamp);
	return lamp;
}

var Turn_On_Lights = function() {
	for (var i = 0; i < lights.length; i++) {
    	lights[i].interact();
	}
}

//placing lamps
var living1 = mkLamp();
scene.add(living1);
living1.position.set(-2.5, 3, 34);

var living2 = mkLamp();
scene.add(living2);
living2.position.set(-2.5, 3, 40);

var living3 = mkLamp();
scene.add(living3);
living3.position.set(-2.5, 3, 27);

var myroom = mkLamp();
scene.add(myroom);
myroom.position.set(-2.5, 3, 19);

var Proom = mkLamp();
scene.add(Proom);
Proom.position.set(-2.5, 3, 7);

var kitchen1 = mkLamp();
scene.add(kitchen1);
kitchen1.position.set(-17, 3, 5);

var kitchen2 = mkLamp();
scene.add(kitchen2);
kitchen2.position.set(-17, 3, 11);

var kitchen3 = mkLamp();
scene.add(kitchen3);
kitchen3.position.set(-17, 3, 17);

var kitchen4 = mkLamp();
scene.add(kitchen4);
kitchen4.position.set(-12, 3, 19);

var living4 = mkLamp();
scene.add(living4);
living4.position.set(-10, 3, 34);

var living5 = mkLamp();
scene.add(living5);
living5.position.set(-10, 3, 40);

var living6 = mkLamp();
scene.add(living6);
living6.position.set(-10, 3, 27);