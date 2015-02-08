/* 
 * A web socket server for a raspberry pi remote controlled car controller page
 * 
 * Douglas Lenz, 2015
 *
 */

var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var piblaster = require('pi-blaster.js');

var beforeDie = function() {
    piblaster.setPwm(4, 0);
}

app.use('/vendor', express.static(__dirname + '/vendor'));
app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket) {
    socket.on('update', function(data) {
	piblaster.setPwm(4, data.gamma);
    });
    socket.on('disconnect', beforeDie);
});

http.listen(3000, function() {
    console.log('Web server listening on *:3000');
});

/*
 * piblaster pin reference
 */

/*   
 *   GPIO number   Pin in P1 header
 *         4              P1-7
 *         17             P1-11
 *         18             P1-12
 *         21             P1-13
 *         22             P1-15
 *         23             P1-16
 *         24             P1-18
 *         25             P1-22
 *
 */
