function mkDoor(width, height, thickness, isNormal, texture) {
	var door_hull_geom = new THREE.BoxGeometry(width, thickness, height);
	var door_hull = createMesh(door_hull_geom, texture, false, null);
	var support1_G = new THREE.CylinderGeometry(0.04, 0.04, 0.3);
	var support1 = createMesh(support1_G, "door_handle.jpg",false,null);
	support1.rotation.x = Math.PI / 2;
	support1.position.set(width / 2, 0, 0.7);
	door_hull.add(support1);
	var support2 = support1.clone();
	support2.position.z = -0.7;
	door_hull.add(support2);
	var handle = createMesh(new THREE.CylinderGeometry(0.02, 0.02, 0.2), "door_handle.jpg",false,null);
	handle.position.set(-width * 0.4, 0, -height * 0.05);
	var handle_p1 = createMesh(new THREE.TorusGeometry(0.1, 0.02, 8, 6, Math.PI / 2), "door_handle.jpg",false,null);
	handle_p1.rotation.y = Math.PI;
	handle_p1.position.set(0.1, 0.1, 0);
	handle.add(handle_p1);
	var handle_p2 = createMesh(new THREE.CylinderGeometry(0.02, 0.02, 0.15), "door_handle.jpg",false,null);
	handle_p2.rotation.z = Math.PI / 2;
	handle_p2.position.set(0.175, 0.2, 0);
	handle.add(handle_p2);
	var handle_p3 = createMesh(new THREE.TorusGeometry(0.1, 0.02, 8, 6, Math.PI / 2), "door_handle.jpg",false,null);
	handle_p3.rotation.z = Math.PI;
	handle_p3.position.set(0.1, -0.1, 0);
	handle.add(handle_p3);
	var handle_p4 = handle_p2.clone();
	handle_p4.position.y = -0.2;
	handle.add(handle_p4);
	var handle_p5 = createMesh(new THREE.CylinderGeometry(0.06, 0.06, 0.13, 24, 24), "door_handle.jpg",false,null);
	handle.position.set(-width * 0.4, 0, -height * 0.05);
	handle.add(handle_p5);
	door_hull.add(handle);
	var hook = new THREE.Object3D();
	door_hull.position.x = -width / 2;
	door_hull.position.z = height / 2;
	hook.add(door_hull);
	// interaction
	toIntersect.push(door_hull);
	door_hull.isOpen = false;
	door_hull.interact = function() {
		applyDoorAnimations(this, isNormal);
		if (!this.isOpen) {
			doorHandleOpenTween.start();
			doorOpenTween.start();
			door_close_sound.stop();
			door_open_sound.play();
			this.isOpen = true;
		} else {
			doorCloseTween.start();
			door_open_sound.stop();
			door_close_sound.play();
			this.isOpen = false;
		}
	}

	var full_door = new THREE.Object3D();
	full_door.add(hook);
	full_door.rotation.x = Math.PI/2;
	if(isNormal===1) {
		full_door.rotation.z = Math.PI/2;
	}
	return full_door;
}

//placing doors
var livingroom = mkDoor(1, 2.5, 0.1, 1, "door.jpg");
livingroom.position.set(-6.6, 3, 34.5);
scene.add(livingroom);

var Vroom = mkDoor(1, 2.5, 0.1, 1, "door.jpg");
Vroom.position.set(-6.6, 3, 19.5);
scene.add(Vroom);

var Nroom = mkDoor(1, 2.5, 0.1, 1, "door.jpg");
Nroom.position.set(-6.6, 3, 10.25);
scene.add(Nroom);

var Broom = mkDoor(1, 2.5, 0.1, -1, "door.jpg");
Broom.position.set(-7.2, 3, 2.2);
scene.add(Broom);

var BAroom = mkDoor(1, 2.5, 0.1, -1, "vetrata.jpg");
BAroom.position.set(-17.3, 3, 2.5);
scene.add(BAroom);

var room = mkDoor(1, 2.5, 0.1, -1, "door_blind.jpg");
room.position.set(-9.6, 2.8, 42);
scene.add(room);