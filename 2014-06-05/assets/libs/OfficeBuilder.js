/*
AUTHOR: Nicola Russo - 433040
-------------------------------------------------------------------------------------


Crea piano 3d con 2 sfere 
*/
function mkDesk3D(width, height, depth, widthSegments, heightSegments, depthSegments) {

	var geometry = new THREE.BoxGeometry(width, height, depth, widthSegments, heightSegments, depthSegments);
	//color: Green
	var material = new THREE.MeshPhongMaterial( {color: 0x00cc00, specular: 0x00cc00 , metal: true, side: THREE.FrontSide} );
	var surface = new THREE.Mesh( geometry, material );
	//surface.castShadow = true;
	surface.receiveShadow = true;

	var geometry = new THREE.SphereGeometry( 1, 32, 32 );
	var material = new THREE.MeshPhongMaterial( {color: 0x99FFFF, specular: 0x99FFFF , metal: true, side: THREE.DoubleSide} );
	var sphere1 = new THREE.Mesh( geometry, material );
	sphere1.castShadow = true;
	//sphere1.receiveShadow = true;

	var geometry1 = new THREE.SphereGeometry( 1, 32, 32 );
	var material1 = new THREE.MeshPhongMaterial( {color: 0xFF0000, specular: 0xFF0000 , metal: true, side: THREE.DoubleSide} );
	var sphere2 = new THREE.Mesh( geometry1, material1 );
	sphere2.castShadow = true;
	sphere2.receiveShadow = true;

	//mk legs
	var mat = new THREE.MeshPhongMaterial( {color: 0x996633, specular: 0x996633 , metal: true, side: THREE.DoubleSide} );
	var geom = new THREE.BoxGeometry(1, 1, 8, 10, 10, 10);
	
	var leg0 = new THREE.Mesh(geom,mat);
	var leg1 = new THREE.Mesh(geom,mat);
	var leg2 = new THREE.Mesh(geom,mat);
	var leg3 = new THREE.Mesh(geom,mat);

	//set positions
	leg0.position.set((width/2)-0.6,(height/2)-0.6,-4);
	leg1.position.set(-(width/2)+0.6,-(height/2)+0.6,-4);
	leg2.position.set(-(width/2)+0.6,(height/2)-0.6,-4);
	leg3.position.set((width/2)-0.6,-(height/2)+0.6,-4);

	//assembly legs
	surface.add(leg0);
	surface.add(leg1);
	surface.add(leg2);
	surface.add(leg3);

	sphere1.position.x = 4;
	sphere1.position.y = 3.5;
	sphere2.position.x = 0;
	sphere2.position.y = -5;
	sphere1.position.z = 1.5;
	sphere2.position.z = 1.5;

	surface.add(sphere2);

	surface.add(sphere1);

	//set properties
	surface.sphereBlue = sphere1;
	surface.sphereRed = sphere2;

	return surface
}
/*
crea pavimento in legno
*/
function mkFloor(width, height) {
	var plane = createMesh(new THREE.PlaneGeometry(width, height), "floor-wood.jpg");
	return plane;
}
/*
crea muro in mattoncini
*/
function mkWall(width, height) {
	var wall = createMesh(new THREE.PlaneGeometry(width, height), "stone-bump.jpg");
	return wall;
}

function createMesh(geom, imageFile) {
        var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + imageFile)
        var mat = new THREE.MeshPhongMaterial();
        mat.map = texture;
        var mesh = new THREE.Mesh(geom, mat);
        return mesh;
}

/*
Crea Lampada
*/
function mkLamp(scaleFactor, lightColor) {

	//init final obj
	var lamp = THREE.Object3D();

	//make base
	var geometry = new THREE.CylinderGeometry( 1.5, 2, 1, 32);
	var material = new THREE.MeshPhongMaterial( {color: 0x999999, specular: 0x999999, shininess: 80} );
	var base = new THREE.Mesh(geometry, material);
	base.rotation.x = Math.PI/2;

	//make and hook arms
	var arm0 = mkBasicJoint(0.5,2.5);

	base.add(arm0);

	arm0.position.y = 1;

	var arm1 = mkBasicJoint(0.5,2.5);

	arm1.position.y = 2.7;

	arm0.hook.add(arm1);

	//make and hook ceiling and bulb
	var ceiling = mkCeiling(lightColor);

	arm1.hook.add(ceiling);

	ceiling.position.y = 2.7;

	lamp = base;
	//set properties
	lamp.basePivot = arm0.sphere;
	lamp.arm0 = arm0.cylinder;
	lamp.arm1 = arm1.cylinder;
	lamp.arm1.sphere = arm1.sphere;
	lamp.ceiling = ceiling;
	return lamp;
}

function mkCeiling(colorLight) {

	var plafonieraGeometry = new THREE.SphereGeometry(1,32,32,0,Math.PI);
	var plafonieraMaterial = new THREE.MeshPhongMaterial({color: 0xc6c6c6, shininess: 80, specular: 0xc6c6c6, side: THREE.DoubleSide, metal:true});

	var plafoniera = new THREE.Mesh(plafonieraGeometry,plafonieraMaterial);
	plafoniera.position.set(0,1.5,0);
	plafoniera.castShadow = true;
	plafoniera.receiveShadow = true;
	plafoniera.rotation.x = Math.PI/2

	var bulbGeometry = new THREE.SphereGeometry(0.2,32,32);
	var bulbMaterial = new THREE.MeshPhongMaterial({color: 0xffef47, transparent:true, opacity:0.5,  wireframe: false});
	var bulb = new THREE.Mesh(bulbGeometry,bulbMaterial);
	var cilindroGeometry = new THREE.CylinderGeometry(0.1,0.2,0.5,16);
	var cilindroMaterial = new THREE.MeshPhongMaterial({color:0x7a7a7a});
	var cilindro = new THREE.Mesh(cilindroGeometry,cilindroMaterial);

	cilindro.rotation.x = Math.PI/2;
	plafoniera.add(cilindro);
	cilindro.position.set(0,0,0.6);

	//make light and target
	var spotlight = new THREE.SpotLight(colorLight, 2);
	spotlight.castShadow = true;
	spotlight.position.set(0,0,0.2);
	//spotlight.shadowCameraVisible = true;
	spotlight.shadowCameraNear = 1;
	// spotlight.shadowMapWitdh = 512;
	// spotlight.shadowMapHeight = 512;
	// spotlight.shadowCameraFOV = 600
	spotlight.angle = Math.PI/2

	var lightTarget = new THREE.Object3D();
	lightTarget.position.set(0,0,-6);
	bulb.add(lightTarget);
	spotlight.target = lightTarget;

	//assembly ceiling
	bulb.add(spotlight);
	plafoniera.add(bulb);	
	bulb.position.set(0,0,0.1)

	var pivot = new THREE.Object3D();
	var sphereGeometry = new THREE.SphereGeometry(0.5, 32, 32);
	var sphereMaterial = new THREE.MeshPhongMaterial({color: 0xdddd33, specular: 0xdddd33, shininess: 80, shading: THREE.FlatShading});
	var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
	sphere.add(plafoniera);
	pivot.add(sphere);

	//set property
	pivot.spotlight = spotlight;

	return pivot;
}


/*
Restituisce un join tra una sfera e 2 cilindro + hook.
*/
function mkBasicJoint (radius, height) {

	var joint = new THREE.Object3D();
	var sphereGeometry = new THREE.SphereGeometry(radius, 32, 32);
	var sphereMaterial = new THREE.MeshPhongMaterial({color: 0xdddd33, specular: 0xdddd33, shininess: 80, shading: THREE.FlatShading});
	var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
	sphere.position.set(0, 0, 0);
	joint.add(sphere);

	var cylinderGeometry = new THREE.CylinderGeometry(radius*0.3, radius*0.3, height, 8, 8, false);
	var cylinderMaterial = new THREE.MeshPhongMaterial({color: 0x999999, specular:0x999999, shininess: 80, shading: THREE.FlatShading});
	var cylinder1 = new THREE.Mesh(cylinderGeometry, cylinderMaterial);
	var cylinder2 = new THREE.Mesh(cylinderGeometry, cylinderMaterial);

	var cyBaseGeom = new THREE.CylinderGeometry(radius, radius/2, 0.5, 8, 8, false);
	var cyBaseMaterial = new THREE.MeshPhongMaterial({color: 0x999999, shading: THREE.FlatShading, specular: 0x999999, shininess: 80});
	
	var cyBaseDown = new THREE.Mesh(cyBaseGeom, cyBaseMaterial);

	var cyBaseGeom = new THREE.CylinderGeometry(radius/2, radius, 0.5, 8, 8, false);

	var cyBaseUp = new THREE.Mesh(cyBaseGeom, cyBaseMaterial);
	
	cylinder1.position.set(0.3, height / 2 + radius -0.3, 0);
	cylinder2.position.set(-0.3, height / 2 + radius -0.3, 0);
	cyBaseDown.position.set(0, height / 2 + radius - 1, 0)
	cyBaseUp.position.set(0, height + radius, 0)

	cyBaseDown.add(cylinder1);
	cyBaseDown.add(cylinder2);
	cyBaseDown.add(cyBaseUp);

	var cylinder = new THREE.Object3D();

	cylinder.add(cyBaseDown);
	sphere.add(cylinder);


	var hook = new THREE.Object3D();
	hook.position.set(0, height/2+radius, 0);
	cylinder.add(hook);

	//Set properties
	joint.sphere = sphere;
	joint.cylinder = cylinder;
	joint.hook = hook;

	return joint;
}