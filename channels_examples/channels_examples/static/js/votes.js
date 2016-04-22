$(function() {

    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var ws_path = ws_scheme + '://' + window.location.host + "/app1/votes/notification";
    console.log("Connecting to " + ws_path);
    var socket = new ReconnectingWebSocket(ws_path);    
    
    socket.onmessage = function(message) {
        console.log("Got message " + message.data);
        var data = JSON.parse(message.data);
        document.getElementById(data.item).innerHTML = data.no_of_votes;
    };

    socket.onopen = function() { console.log("Connected to notification socket"); }
    socket.onclose = function() { console.log("Disconnected to notification socket"); }

    $('button[name="btnSubmit"]').click(function(){
        var val = $(this).attr("value");
        socket.send(val);
    });
});