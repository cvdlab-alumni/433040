//load dwelling
var loader = new THREE.OBJLoader();
var dwelling;

loader.load('assets/models/master.obj', function (obj) {

    var multiMaterial = [
    new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}),
    new THREE.MeshBasicMaterial({ overdraw: true, color: 0xffffff, side: THREE.DoubleSide})
    ];

    mesh = THREE.SceneUtils.createMultiMaterialObject(obj.children[0].geometry, multiMaterial);
    mesh.rotation.x = -Math.PI/2;
    mesh.rotation.z = Math.PI;
    dwelling = mesh;
    scene.add(dwelling);

    //mk missed walls
    var missed_walls = mkCompleteDwellingsWalls(multiMaterial);
    for (var i = missed_walls.length - 1; i >= 0; i--) {
    scene.add(missed_walls[i]);
    };

    var geometry = new THREE.BoxGeometry(20.8, 2, 41.8);
    //floor
    var texture = THREE.ImageUtils.loadTexture("assets/textures/general/floor-wood.jpg");
    //texture.needsUpdate = true;
    texture.wrapS = THREE.RepeatWrapping;
    texture.wrapT = THREE.RepeatWrapping;
    var mat = new THREE.MeshPhongMaterial();
    var surface = new THREE.Mesh(geometry, mat);
    surface.material.map = texture;
    surface.material.needsUpdate = true;
    //set params for repeat texture
    surface.material.map.repeat.set(10, 10);
    surface.material.map.wrapS = THREE.RepeatWrapping;
    surface.material.map.wrapT = THREE.RepeatWrapping;

    surface.rotation.x = Math.PI/2;
    surface.position.set(10.5,21,0);
    mesh.add(surface);

    //ground
    var geometry1 = new THREE.BoxGeometry(21, 2, 5);
    var surface1 = createMesh(geometry1, "stone.jpg", true, "stone-test.jpg");
    surface1.material.map.repeat.set(1,1);
    surface1.material.map.wrapS = THREE.RepeatWrapping;
    surface1.material.map.wrapT = THREE.RepeatWrapping;
    surface1.rotation.x = Math.PI/2;
    mesh.add(surface1);
    surface1.position.set(10.5,44.5,0);

    //garden 
    var geometry2 = new THREE.BoxGeometry(100, 100, 0.1);
    var surface2 = createMesh(geometry2, "green.jpg", false, null);
    surface2.material.map.repeat.set(1,1);
    surface2.material.map.wrapS = THREE.RepeatWrapping;
    surface2.material.map.wrapT = THREE.RepeatWrapping;
    mesh.add(surface2);
    surface2.position.set(13,16,0);
});
