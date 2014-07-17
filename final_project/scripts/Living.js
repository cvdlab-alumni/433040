//Sofa
function mkSofa(xPos,yPos,zPos)
{
      var SofaGeom = new THREE.BoxGeometry(1.5,0.3,1);
      var sofa = createMesh(SofaGeom, "sofa.jpg", false, null);
      //mk arms
      var sofa_armDX_Geom = new THREE.CylinderGeometry(0.2, 0.2, 1, 32);
      var sofa_armDX = createMesh(sofa_armDX_Geom, "sofa.jpg", false, null);
      sofa.add(sofa_armDX);
      sofa_armDX.position.set(0.75,0.2,0);
      sofa_armDX.rotation.x = Math.PI/2;
      var sofa_armSX_Geom = new THREE.CylinderGeometry( 0.2, 0.2, 1, 32);
      var sofa_armSX = createMesh(sofa_armSX_Geom, "sofa.jpg", false, null);
      sofa.add(sofa_armSX);
      sofa_armSX.position.set(-0.75,0.2,0);
      sofa_armSX.rotation.x = Math.PI/2;
      //mk top
      var sofa_T_geom = new THREE.BoxGeometry(1.5,0.7,0.2);
      var sofa_T = createMesh(sofa_T_geom, "sofa.jpg", false, null);
      sofa.add(sofa_T);
      sofa_T.position.set(0,0.5,0.43);
      //mk feet
      var sofa_foot_Geom = new THREE.CylinderGeometry( 0.05, 0.05, 0.5, 32);
      var mat = new THREE.MeshPhongMaterial( {color: 0x999999, specular: 0x999999 , metal: true, side: THREE.DoubleSide} );
      var sofa_foot0 = new THREE.Mesh(sofa_foot_Geom,mat);
      sofa.add(sofa_foot0);
      sofa_foot0.position.set(0.70,-0.1,0.45);
      var sofa_foot1 = new THREE.Mesh(sofa_foot_Geom,mat);
      sofa.add(sofa_foot1);
      sofa_foot1.position.set(-0.70,-0.1,0.45);
      var sofa_foot2 = new THREE.Mesh(sofa_foot_Geom,mat);
      sofa.add(sofa_foot2);
      sofa_foot2.position.set(-0.70,-0.1,-0.45);
      var sofa_foot3 = new THREE.Mesh(sofa_foot_Geom,mat);
      sofa.add(sofa_foot3);
      sofa_foot3.position.set(0.70,-0.1,-0.45);
      sofa.position.set(xPos,yPos,zPos);
      return sofa;
}

//placing sofa
var sofa0 = mkSofa(-3,1.3,40);
scene.add(sofa0);

//carpets

var CarpetGeom = new THREE.BoxGeometry(2.5,0.1,1.5);
var carpet = createMesh(CarpetGeom, "carpet.jpg", false, null);
scene.add(carpet);
carpet.position.set(-3,1,38.5);

var CarpetGeom1 = new THREE.BoxGeometry(2.5,0.1,5);
var carpet1 = createMesh(CarpetGeom1, "carpet2.jpg", false, null);
carpet1.position.set(-3,1,32);
scene.add(carpet1);
//

//table
var surface = mkTable();
scene.add(surface);
surface.position.set(-3, 1.5,32);
//add flowers
var flowers = mkFlowers();
flowers.scale.set(0.1,0.1,0.1);
surface.add(flowers);
flowers.position.set(0,0.2,0);
//

//pictures
var picture_picasso = mkPict("framePers.jpg","bumpFrame.jpg");
scene.add(picture_picasso);
picture_picasso.rotation.z = -Math.PI/2;
picture_picasso.rotation.x = Math.PI/2;
picture_picasso.position.set(-5.75,2,38);
//

//tv with video texture

//load obj by Id
var texture;
var $video = $('#video');
var video = $video[0];
//set texture proprerties 
texture = new THREE.Texture(video);
texture.minFilter = THREE.LinearFilter;
texture.magFilter = THREE.LinearFilter;
texture.format = THREE.RGBFormat;
texture.generateMipmaps = false;
//assembly TV
var tv;
var content;
var geom = new THREE.BoxGeometry(2.1,1.2,0.1);
content = createMesh(geom, "tv.jpg", false, null);
tv = createTV(new THREE.BoxGeometry(2, 1.1, 0.01));
content.add(tv);
tv.position.z = 0.1;
scene.add(content);
content.position.set(-3,2,23.7);
tv.visible = false;
tv.isOn = false;
toIntersect.push(tv);
tv.interact = function() {
      if(!this.isOn)
      {
            tv.visible = true;
            video.play();
            this.isOn = true;
      }
      else
      {
            tv.visible = false;
            video.pause();
            this.isOn = false;
      }
}


function createTV (geom) {
    var materialArray = [];
    materialArray.push(new THREE.MeshBasicMaterial({ color: 0xaaaaaa  }));
    materialArray.push(new THREE.MeshBasicMaterial({ color: 0xaaaaaa  }));
    materialArray.push(new THREE.MeshBasicMaterial({ color: 0xaaaaaa  }));
    materialArray.push(new THREE.MeshBasicMaterial({ color: 0xaaaaaa   }));
    materialArray.push(new THREE.MeshBasicMaterial({ map: texture }));
    materialArray.push(new THREE.MeshBasicMaterial({ color: 0xaaaaaa  }));
    var faceMaterial = new THREE.MeshFaceMaterial(materialArray);

    // create a multimaterial
    var mesh = new THREE.Mesh(geom, faceMaterial);

    return mesh;
}