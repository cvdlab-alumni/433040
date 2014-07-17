var disableLights = false;

function onDocumentMouseDown(event) {
	event.preventDefault();
	if (document.pointerLockElement === element || document.mozPointerLockElement === element || document.webkitPointerLockElement === element) {
		var vector = new THREE.Vector3(0, 0, 0.5);
		projector.unprojectVector(vector, camera);
		var raycaster = new THREE.Raycaster(vector,
			controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
	} else {
		var vector = new THREE.Vector3((event.clientX / window.innerWidth) * 2 - 1, -(event.clientY / window.innerHeight) * 2 + 1, 0.5);
		projector.unprojectVector(vector, camera);
		var raycaster = new THREE.Raycaster(camera.position,
			vector.sub(camera.position).normalize());

	}
	var intersects = raycaster.intersectObjects(toIntersect);
	if (intersects.length > 0) {
		intersects[0].object.interact && intersects[0].object.interact();
	}
}

function onWindowResize() {
	camera.aspect = window.innerWidth / window.innerHeight;
	camera.updateProjectionMatrix();
	renderer.setSize(window.innerWidth, window.innerHeight);
}

var scene = new THREE.Scene();

var axis = new THREE.AxisHelper(5000);
scene.add(axis);


// camera
var camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.up = new THREE.Vector3(0, 1, 0);
camera.position.set(0, 14, 70);
camera.lookAt(scene.position);
scene.add(camera);


// directional light
dirLight = new THREE.DirectionalLight('#FFFFFF', 0.8);
dirLight.position.set(-20, 50, 10);
scene.add(dirLight);


// renderer
var renderer = new THREE.WebGLRenderer();
renderer.setClearColor(new THREE.Color('#000000'));
renderer.setSize(window.innerWidth, window.innerHeight);
window.addEventListener('resize', onWindowResize, false);

// trackball controls
var trackballControls = new THREE.TrackballControls(camera);

// mouse interaction
var projector = new THREE.Projector();
document.addEventListener('mousedown', onDocumentMouseDown, false);
var toIntersect = [];

// first person controls
var FPenabled = false;
var controls;
var objects = [];
var rayMove = new THREE.Raycaster();
rayMove.ray.direction.set(0, 0, -1);
var rayPointer = new THREE.Raycaster();

// for texture
function createMesh(geom, texture, isbump, bump) {
var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + texture)
texture.wrapS = THREE.RepeatWrapping;
texture.wrapT = THREE.RepeatWrapping;

geom.computeVertexNormals();
var mat = new THREE.MeshPhongMaterial();
mat.map = texture;

if (isbump) {
  var bump_ = THREE.ImageUtils.loadTexture("assets/textures/general/" + bump);
  mat.bumpMap = bump_;
  mat.bumpScale = 0.2;
}

var mesh = new THREE.Mesh(geom, mat);

return mesh;
}

function initStats() {
	var stats = new Stats();
	stats.setMode(0);
	$('#stats').append(stats.domElement);
	return stats;
}

var stats = initStats();

function animate() {
	requestAnimationFrame(animate);
	render();
	update();
}

function update() {
	// stats
	stats.update();
	// animations
	TWEEN.update();
	// control gui
	if (controls.enableTrackball) {
		trackballControls.update();
	}
	// first person controls
	if (FPenabled === true) {
		computeFPControls();
	}
    //tv

    if (video.readyState === video.HAVE_ENOUGH_DATA) {
          if (texture) texture.needsUpdate = true;
    }
}

function render() {

	renderer.render(scene, camera);
}