from channels import include


channel_routing = [
    include("app1.routing.post_websocket", path=r"^/app1/posts/notification"),
    include("app1.routing.vote_websocket", path=r"^/app1/votes/notification"),
]
