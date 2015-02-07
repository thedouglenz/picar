/*
 * WebSocket connection class
 * Douglas Lenz
 * 2015
 */

function WebsocketConnection() {
    this.ws = new WebSocket("wss://" + location.host + "/picar");

    this.ready = function() {
	return this.ws.readyState === 1 ? true : false;
    }

    this.sendObject = function(obj) {
	if(this.ready()) {
	    this.ws.send(JSON.stringify(obj));
	}
    }
}
