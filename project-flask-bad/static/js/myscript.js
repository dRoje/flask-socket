
var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function () {
    socket.emit('connection', {data: 'I\'m connected!'});
});

socket.on("sliderValue", function (msg) {
    document.getElementById("rangeSlider").value = msg;
    document.getElementById("lightOn").style.opacity = msg/100;
});