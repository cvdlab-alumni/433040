//import kitchen and placing
var kitchen = importObj('doppio.obj', 'doppio.mtl',false);
kitchen.scale.set(0.014, 0.014, 0.014);
kitchen.rotation.y = Math.PI / 2;
scene.add(kitchen);
kitchen.position.set(-18.1, 1, 9);

var kitchen_gas = importObj('largeStove.obj', 'largeStove.mtl',false);
kitchen_gas.scale.set(0.014, 0.014, 0.014);
kitchen_gas.rotation.y = Math.PI / 2;
scene.add(kitchen_gas);
kitchen_gas.position.set(-20.2, 1, 7.8);

var kitchen_lavello = importObj('lavello.obj', 'lavello.mtl',false);
kitchen_lavello.scale.set(0.014, 0.014, 0.014);
kitchen_lavello.rotation.y = -Math.PI / 2;
scene.add(kitchen_lavello);
kitchen_lavello.position.set(-15.8, 1, 7.8);

var kitchen_s = importObj('pensileDoppio.obj', 'pensileDoppio.mtl',false);
kitchen_s.scale.set(0.014, 0.014, 0.014);
kitchen_s.rotation.y = -Math.PI / 2;
scene.add(kitchen_s);
kitchen_s.position.set(-13.9, 0.0003, 8.3);

var surface = mkTable();
scene.add(surface);
surface.position.set(-18, 1.5,20);

var wine = importObj('red-wine-bottle-01.obj', 'red-wine-bottle-01.mtl',false);
wine.scale.set(0.014, 0.014, 0.014);
surface.add(wine);
wine.position.y = 0.25;

var fridge = importObj('frigo.obj', 'frigo.mtl',false);
fridge.scale.set(0.01, 0.01, 0.01);
fridge.position.set(-21.5, 1,20);
fridge.rotation.y = Math.PI / 2;
scene.add(fridge);
