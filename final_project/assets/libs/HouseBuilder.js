function mkCompleteDwellingsWalls(material) {
	
  var result = new Array();

  var geom = new THREE.BoxGeometry(0.8,4,14);
  var wall_cameraAnto = new THREE.Mesh( geom,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto.position.set(-6.2,1,26.5);
  result.push(wall_cameraAnto);

  var geom2 = new THREE.BoxGeometry(0.8,4,8.5);
  var wall_cameraAnto2 = new THREE.Mesh( geom2,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto2.position.set(-6.2,1,14.5);
  result.push(wall_cameraAnto2);

  var geom3 = new THREE.BoxGeometry(0.8,4,7.5);
  var wall_cameraAnto3 = new THREE.Mesh( geom3,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto3.position.set(-6.2,1,5.5);
  result.push(wall_cameraAnto3);

  var geom4 = new THREE.BoxGeometry(0.8,4,7);
  var wall_cameraAnto4 = new THREE.Mesh( geom4,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto4.position.set(-6.2,1,38);
  result.push(wall_cameraAnto4);

  var geom5 = new THREE.BoxGeometry(0.8,0.4,40);
  var wall_cameraAnto5 = new THREE.Mesh( geom5,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto5.position.set(-6.2,2.8,21.5);
  result.push(wall_cameraAnto5);

  var geom6 = new THREE.BoxGeometry(0.8,0.4,3);
  var wall_cameraAnto6 = new THREE.Mesh( geom6,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto6.position.set(-9,2.8,21.5);
  result.push(wall_cameraAnto6);

  var geom7 = new THREE.BoxGeometry(0.8,4,4.7);
  var wall_cameraAnto7 = new THREE.Mesh( geom7,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto7.position.set(-9,1,17.8);
  result.push(wall_cameraAnto7);

  var geom8 = new THREE.BoxGeometry(2.9,4,0.8);
  var wall_cameraAnto8 = new THREE.Mesh( geom8,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto8.position.set(-8,1,22.8);
  result.push(wall_cameraAnto8);

  var geom9 = new THREE.BoxGeometry(8.3,4,0.8);
  var wall_cameraAnto9 = new THREE.Mesh( geom9,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto9.position.set(-16.7,1,22.8);
  result.push(wall_cameraAnto9);

  var geom10 = new THREE.BoxGeometry(8.3,0.4,0.5);
  var wall_cameraAnto10 = new THREE.Mesh( geom10,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto10.position.set(-16.7,2.8,2.2);
  result.push(wall_cameraAnto10);

  var geom11 = new THREE.BoxGeometry(7,4,0.5);
  var wall_cameraAnto11 = new THREE.Mesh( geom11,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto11.position.set(-13.9,1,2.2);
  result.push(wall_cameraAnto11);

  var geom12 = new THREE.BoxGeometry(2.5,4,0.5);
  var wall_cameraAnto12 = new THREE.Mesh( geom12,new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}));
  wall_cameraAnto12.position.set(-19.5,1,2.2);
  result.push(wall_cameraAnto12);

  return result;
}

function mkDesk3D(width, height, depth, surface) {
  //mk legs
  var mat = new THREE.MeshPhongMaterial( {color: 0x999999, specular: 0x999999 , metal: true, side: THREE.DoubleSide} );
  var geom = new THREE.BoxGeometry(1, 1, 8, 10, 10, 10);
  
  var leg0 = new THREE.Mesh(geom,mat);
  var leg1 = new THREE.Mesh(geom,mat);
  var leg2 = new THREE.Mesh(geom,mat);
  var leg3 = new THREE.Mesh(geom,mat);

  //assembly legs
  surface.add(leg0);
  surface.add(leg1);
  surface.add(leg2);
  surface.add(leg3);

    //set positions
  leg0.position.set((width/2)-0.6,-4,(depth/2)-0.6);
  leg1.position.set(-(width/2)+0.6,-4,-(depth/2)+0.6);
  leg2.position.set(-(width/2)+0.6,-4,(depth/2)-0.6);
  leg3.position.set((width/2)-0.6,-4,-(depth/2)+0.6);
  leg0.rotation.x = Math.PI/2;
  leg1.rotation.x = Math.PI/2;
  leg2.rotation.x = Math.PI/2;
  leg3.rotation.x = Math.PI/2;

  return surface
}

function mkBed() {
  var geom_base = new THREE.BoxGeometry(32,5,23);
  var geom_mattress = new THREE.BoxGeometry(27,7,18);
  var pillow_geom = new THREE.BoxGeometry(5,9,12);
  var base_bed = createMesh(geom_base, "legnoLetto.jpg", false, null);
  var mattress = createMesh(geom_mattress, "mattress.jpg", false, null);
  var pillow = createMesh(pillow_geom, "pillow.jpg", false, null);
  mattress.add(pillow);
  pillow.position.set(9,0,0);
  base_bed.add(mattress);  
  return base_bed;
}

function mkTable() {
      var width = 1.5;
      var depth = 3;
      var table_geom = new THREE.BoxGeometry(width,0.1,depth);
      surface = createMesh(table_geom, "tavolo.jpg", false, null);
      //mk legs
      var mat = new THREE.MeshPhongMaterial( {color: 0x999999, specular: 0x999999 , metal: true, side: THREE.DoubleSide} );
      var geom = new THREE.BoxGeometry(0.1, 0.1, 1, 10, 10, 10);
      var leg0 = new THREE.Mesh(geom,mat);
      var leg1 = new THREE.Mesh(geom,mat);
      var leg2 = new THREE.Mesh(geom,mat);
      var leg3 = new THREE.Mesh(geom,mat);
      //assembly legs
      surface.add(leg0);
      surface.add(leg1);
      surface.add(leg2);
      surface.add(leg3);
      //set positions
      leg0.position.set((width/2)-0.1,-0.5,(depth/2)-0.1);
      leg1.position.set(-(width/2)+0.1,-0.5,-(depth/2)+0.1);
      leg2.position.set(-(width/2)+0.1,-0.5,(depth/2)-0.1);
      leg3.position.set((width/2)-0.1,-0.5,-(depth/2)+0.1);
      leg0.rotation.x = Math.PI/2;
      leg1.rotation.x = Math.PI/2;
      leg2.rotation.x = Math.PI/2;
      leg3.rotation.x = Math.PI/2;
      surface.position.y = -3;
      return surface;
    }

  function mkFlowers() {
    var flowers_geom = new THREE.CylinderGeometry(1, 1, 4.3, 8, 8, false);
      var flowers = createMesh(flowers_geom, "vaso.jpg", false, null);
      flowers.position.y = 3;
      //assembly flowers
      var flower_geom = new THREE.SphereGeometry(0.5, 32, 32);
      var leaf_geom = new THREE.CylinderGeometry(0.1, 0.1, 5, 8, 8, false);
      var material = new THREE.MeshPhongMaterial( {color: 0x1BBF26, specular: 0x1BBF26 , metal: true, side: THREE.DoubleSide} );
      var leaf0 = new THREE.Mesh(leaf_geom,material);
      var flower0 = createMesh(flower_geom, "vaso1.jpg", false, null);
      leaf0.add(flower0);
      flower0.position.y = 2.7;
      flowers.add(leaf0);
      leaf0.position.y = 1.8;
      var leaf1 = new THREE.Mesh(leaf_geom,material);
      var flower1 = createMesh(flower_geom, "vaso1.jpg", false, null);
      leaf1.add(flower1);
      flower1.position.y = 2.7;
      flowers.add(leaf1);
      leaf1.position.y = 1.3;
      leaf1.position.z = 0.5;
      var leaf2 = new THREE.Mesh(leaf_geom,material);
      var flower2 = createMesh(flower_geom, "vaso1.jpg", false, null);
      leaf2.add(flower2);
      flower2.position.y = 2.7;
      flowers.add(leaf2);
      leaf2.position.y = 1.5;
      leaf2.position.z = -0.5;
      leaf2.position.x = -0.5;
      var leaf3 = new THREE.Mesh(leaf_geom,material);
      var flower3 = createMesh(flower_geom, "vaso1.jpg", false, null);
      leaf3.add(flower3);
      flower3.position.y = 2.7;
      flowers.add(leaf3);
      leaf3.position.y = 1.7;
      leaf3.position.z = -0.5;
      leaf3.position.x = 0.5;
      return flowers;
  }

//function for texture
      function createMesh(geom, texture, isbump, bump) {
        var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + texture);
        texture.needsUpdate = true;
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
        mesh.material.needsUpdate = true;
        return mesh;

      }

function mkPict (frame, bump) {
  var pict_geom = new THREE.BoxGeometry(1.5, 0.05, 1);
  var picture = createMesh(pict_geom, frame, true, bump);
  return picture;
}

function importObj(obj, mtl, doubleSide) {
  var container = new THREE.Object3D();
  var loader = new THREE.OBJMTLLoader();
  loader.addEventListener('load', function(event) {
    var object = event.content;
    if (doubleSide) {
      object.traverse(function(child) {
        if (child instanceof THREE.Mesh) {
          child.material.side = THREE.DoubleSide;
        }
      });
    }
    container.add(object);
  });
  loader.load("assets/models/" + obj,"assets/models/" + mtl);
  return container;
}

//Skybox
function mkDAYskybox()
{
  var directions = ["Dxpos", "Dxneg", "Dzpos", "Dzneg", "Dypos", "Dyneg"];
  var materialArray = [];
  for (var i = 0; i < 6; i++)
    materialArray.push(new THREE.MeshBasicMaterial({
      map: THREE.ImageUtils.loadTexture("assets/textures/general/skybox" + "_" + directions[i] + ".jpg"),
      side: THREE.BackSide
    }));
  var skybox_material = new THREE.MeshFaceMaterial(materialArray);
  var skybox = new THREE.Mesh(new THREE.CubeGeometry(500, 500, 500), skybox_material);
  skybox.color = new THREE.Color('#FFFFFF');
  skybox.name = "sky";
  return skybox;
}

function mkNIGHTskybox()
{
  var directions = ["Nxpos", "Nxneg", "Nzpos", "Nzneg", "Nypos", "Nyneg"];
  var materialArray = [];
  for (var i = 0; i < 6; i++)
    materialArray.push(new THREE.MeshBasicMaterial({
      map: THREE.ImageUtils.loadTexture("assets/textures/general/skybox" + "_" + directions[i] + ".jpg"),
      side: THREE.BackSide
    }));
  var skybox_material = new THREE.MeshFaceMaterial(materialArray);
  var skybox = new THREE.Mesh(new THREE.CubeGeometry(500, 500, 500), skybox_material);
  skybox.color = new THREE.Color('#FFFFFF');
  skybox.name = "sky";
  return skybox;
}

function importObjMtl(obj, mtl, doubleSide, transformObject) {
  var container = new THREE.Object3D();
  var loader = new THREE.OBJMTLLoader();
  loader.addEventListener('load', function(event) {
    var object = event.content;
    if (doubleSide) {
      object.traverse(function(child) {
        if (child instanceof THREE.Mesh) {
          child.material.side = THREE.DoubleSide;
        }
      });
    }
    if (transformObject) {
      transformObject(object);
    }
    container.add(object);
  });
  loader.load("assets/models/" + obj, "assets/models/" + mtl);
  return container;
}
