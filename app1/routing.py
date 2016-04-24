from channels.routing import route

from . import consumers

post_websocket = [
    route("websocket.connect", consumers.websocket_connect),
    route("websocket.disconnect", consumers.websocket_disconnect)
]


vote_websocket = [
    route("websocket.connect", consumers.websocket_voteconnect),
    route("websocket.receive", consumers.ws_updatevotes),
    route("websocket.disconnect", consumers.websocket_votedisconnect)
]
