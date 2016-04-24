import logging
import json
from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user_from_http

from app1.models import Vote

log = logging.getLogger(__name__)


@channel_session_user_from_http
def websocket_connect(message):
    log.info('websocket_connect. message = %s', message)
    Group("notifications").add(message.reply_channel)


@channel_session
def websocket_disconnect(message):
    log.info('websocket_disconnect. message = %s', message)
    Group("notifications").discard(message.reply_channel)


# VOTES
@channel_session
def websocket_voteconnect(message):
    log.info('websocket_voteconnect. message = %s', message)
    Group("votes").add(message.reply_channel)


@channel_session
def ws_updatevotes(message):
    item = message.content['text']
    vote = Vote.objects.get(item=item)
    vote.number_of_votes += 1
    vote.save()

    data = {
        'no_of_votes': str(vote.number_of_votes),
        'item': str(item)
    }

    Group(
        'votes',
        channel_layer=message.channel_layer
        ).send({'text': json.dumps(data)})


@channel_session
def websocket_votedisconnect(message):
    log.info('websocket_votedisconnect. message = %s', message)
    Group("votes").discard(message.reply_channel)
