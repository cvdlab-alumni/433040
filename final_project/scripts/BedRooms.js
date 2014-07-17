//my room

//bed
var bedA = mkBed();
scene.add(bedA);
bedA.position.set(-3,1.3,15);
bedA.scale.set(0.1,0.1,0.1);
//desk
var surface = mkTable();
scene.add(surface);
surface.position.set(-3, 1.5,10.5);
surface.rotation.y = Math.PI/2;
// pc screen interaction
var pcScreen = createMesh(new THREE.PlaneGeometry(6.5, 4, 1, 1), "framePers.jpg", false, null);
pcScreen.rotation.x = Math.PI / 2;
pcScreen.position.set(2.6, -0.001, 2.5);
pcScreen.isOpen = false;
pcScreen.name = "pc";
toIntersect.push(pcScreen);
pcScreen.interact = function() {
    importPCAnimations(this);
    if (this.isOpen) {
        closePCTween.start();
        this.isOpen = false;
    } else {
        openPCTween.start();
        this.isOpen = true;
    }
}
// pc
var pc_bedroom = importObjMtl('bedroom_laptop.obj', 'bedroom_laptop.mtl', true, function(object) {
    object.remove(object.children[4]);
    object.remove(object.children[3]);
    object.remove(object.children[2]);
    var hook = new THREE.Object3D();
    object.children[1].position.set(0, -0.32, 1.2);
    hook.position.set(0, 0.32, -1.2);
    hook.add(object.children[1]);
    object.remove(object.children[1]);
    hook.add(pcScreen);
    object.add(hook);
});
pc_bedroom.scale.set(0.1, 0.1, 0.1);
surface.add(pc_bedroom);
pc_bedroom.rotation.y = Math.PI / 2;
pc_bedroom.position.set(0, 0.1, 0);
     //pc_bedroom.rotation.x = Math.PI / 2;
    //pc_bedroom.rotation.y = -Math.PI / 2;

//robot function
function mkRobot(xScale,yScale,zScale){
	//make robot arms
    var arm_dx = mkRobotArm(1,6);
    var arm_sx = mkRobotArm(1,6);
    arm_dx.rotation.z = Math.PI/2;
    arm_sx.rotation.z = -Math.PI/2;

    //make robot legs
    leg_dx = mkRobotLeg(1,6);
    leg_sx = mkRobotLeg(1,6);
    leg_dx.rotation.z = Math.PI;
    leg_sx.rotation.z = Math.PI;

    //make robot body and head
    var body = mkRobotBody(2,8);
    
    //assembly robot
    body.hook_tr.add(arm_dx);
    body.hook_tl.add(arm_sx);
    body.hook_br.add(leg_dx);
    body.hook_bl.add(leg_sx);
   	body.scale.set(xScale,yScale,zScale);
   	return body;
}

//robot script (for gui)
var arm_dx = mkRobotArm(1,6);
var arm_sx = mkRobotArm(1,6);
arm_dx.rotation.z = Math.PI/2;
arm_sx.rotation.z = -Math.PI/2;

//make robot legs
leg_dx = mkRobotLeg(1,6);
leg_sx = mkRobotLeg(1,6);
leg_dx.rotation.z = Math.PI;
leg_sx.rotation.z = Math.PI;

//make robot body and head
var body = mkRobotBody(2,8);

//assembly robot
body.hook_tr.add(arm_dx);
body.hook_tl.add(arm_sx);
body.hook_br.add(leg_dx);
body.hook_bl.add(leg_sx);
body.scale.set(0.05,0.05,0.05);
scene.add(body);
body.position.set(-3,2.5,19);


//parents room
var bedB = mkBed();
scene.add(bedB);
bedB.position.set(-3,1.2,4.5);
bedB.scale.set(0.1,0.1,0.1);

var sign = new THREE.BoxGeometry(0.5, 0.01, 0.3);
var sign_ = createMesh(sign, "sign.jpg", false, null);
surface.add(sign_);



sign_.rotation.z = Math.PI/2;
sign_.rotation.x = -Math.PI/2;
sign_.position.set(-1.2,0.8,0);
