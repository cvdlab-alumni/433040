     /*
     AUTHOR: Nicola Russo - 433040
     -------------------------------------------------------
     */

     /*
     Restituisce un join tra una sfera e un cilindro + hook.
     */
     function mkBasicJoint (radius, height) {
     var joint = new THREE.Object3D();
     var sphereGeometry = new THREE.SphereGeometry(radius, 8, 8);
     var sphereMaterial = new THREE.MeshLambertMaterial({color: 0xdddd33, shading: THREE.FlatShading});
     var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
     sphere.position.set(0, 0, 0);
     joint.add(sphere);

     var cylinderGeometry = new THREE.CylinderGeometry(radius, radius, height, 8, 8, false);
     var cylinderMaterial = new THREE.MeshLambertMaterial({color: 0xcccccc, shading: THREE.FlatShading});
     var cylinder = new THREE.Mesh(cylinderGeometry, cylinderMaterial);
     cylinder.position.set(0, height / 2 + radius, 0);
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
     
     /*
     Crea braccio robotico
     */
     function mkRobotArm(radius, height) {
        
        var braccio = mkBasicJoint(radius, height);

        var avambraccio = mkBasicJoint(radius, height);
        braccio.hook.add(avambraccio);

        var dito0 = mkBasicJoint(radius*0.6, height/4);
        avambraccio.hook.add(dito0);

        var dito1 = mkBasicJoint(radius*0.6, height/4);
        avambraccio.hook.add(dito1);

        //set init position
        dito1.rotation.y = 0.9;
        dito1.sphere.rotation.x = 0.7;

        //set properties
        braccio.avambraccio = avambraccio;
        braccio.dito0 = dito0;
        braccio.dito1 = dito1;

        return braccio;
     }

     /*
     Crea gamba robotica
     */
     function mkRobotLeg(radius, height) {
        
        var femore = mkBasicJoint(radius, height);

        var tibia = mkBasicJoint(radius, height);
        femore.hook.add(tibia);

        var piede = mkBasicJoint(radius*1.3, height/5);
        tibia.hook.add(piede);

        //set properties
        femore.tibia = tibia;
        femore.piede = piede;

        return femore;
     }

     /*
     Crea corpo robotico
     */
     function mkRobotBody (radius, height) {

          var joint = new THREE.Object3D();
          var sphereGeometry = new THREE.SphereGeometry(radius, 8, 8);
          var sphereMaterial = new THREE.MeshLambertMaterial({color: 0xdddd33, shading: THREE.FlatShading});
          var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
          sphere.position.set(0, 0, 0);
          joint.add(sphere);

          var cylinderGeometry = new THREE.CylinderGeometry(radius, radius, height, 8, 8, false);
          var cylinderMaterial = new THREE.MeshLambertMaterial({color: 0xcccccc, shading: THREE.FlatShading});
          var cylinder = new THREE.Mesh(cylinderGeometry, cylinderMaterial);
          cylinder.position.set(0, -(height / 2 + radius), 0);
          sphere.add(cylinder);

          var hook_tr = new THREE.Object3D();
          hook_tr.position.set(-1.9, -((-2/3)*height/+radius), 0);
          cylinder.add(hook_tr);

          var hook_tl = new THREE.Object3D();
          hook_tl.position.set(1.9, -((-2/3)*height/+radius), 0);
          cylinder.add(hook_tl);

          var hook_br = new THREE.Object3D();
          hook_br.position.set(-1.9, -(height/+radius), 0);
          cylinder.add(hook_br);

          var hook_bl = new THREE.Object3D();
          hook_bl.position.set(1.9, -(height/+radius), 0);
          cylinder.add(hook_bl);

          //Set properties
          joint.head = sphere;
          joint.trunk = cylinder;
          joint.hook_tr = hook_tr;
          joint.hook_tl = hook_tl;
          joint.hook_br = hook_br;
          joint.hook_bl = hook_bl;

          return joint;
     }