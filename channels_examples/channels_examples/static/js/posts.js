$(function() {

    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var ws_path = ws_scheme + '://' + window.location.host + "/app1/posts/notification";
    console.log("Connecting to " + ws_path);
    var socket = new ReconnectingWebSocket(ws_path);    
    
    socket.onmessage = function(message) {
        console.log("Got message " + message.data);
        var data = JSON.parse(message.data);
        msg = "POST: <b>"+data.post+'</b> has been '+data.type+' by <b>'+data.done_by+'</b> at '+ data.done_at
        document.getElementById("notification").innerHTML = msg;
        document.getElementById("notification").className = 'alert alert-success'
    };

    socket.onopen = function() { console.log("Connected to notification socket"); }
    socket.onclose = function() { console.log("Disconnected to notification socket"); }
});