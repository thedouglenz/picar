/*
 * Keyboard library for picar
 *
 * Douglas lenz
 * 2015
 */

/* Keyboard constants */

K_LEFT = 37;
K_RIGHT = 39;
K_UP = 38;
K_DOWN = 40;
K_A = 65;

var keysDown = new Array(256);
var arrowKeys = [K_UP, K_RIGHT, K_LEFT, K_RIGHT]

var initKeys = function() {
    for(var i=0; i < keysDown.length; i++) {
	keysDown[i] = false;
    }
}

var clear = function(e) {
    keysDown[e.keyCode] = false;
    sendKeys();
}

var updateKeys = function(e) {
    keysDown[e.keyCode] = true;
    sendKeys();
}

var sendKeys = function() {
    var dks = [];
    for(var i=0; i < arrowKeys.length; i++) {
	if(keysDown[arrowKeys[i]] {
	    dks.push(arrowKeys[i]);
	}
    }
    websock.sendObject({'keys' : dks});
}

var keyboard = function() {
    initKeys();
    document.onkeydown = updateKeys;
    document.onkeyup = clearKeys;
}


var up = function() {
    return keysDown[K_UP];
}

var down = function() {
    return keysDown[K_DOWN];
}

var right = function() {
    return keysDown[K_RIGHT];
}

var left = function() {
    return keysDown[K_LEFT];
}
