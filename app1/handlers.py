import logging
import json
from django.dispatch import receiver
from channels import Group
from crudbuilder.signals import(
    post_create_signal,
    post_update_signal
)

from app1.models import Post

logger = logging.getLogger(__name__)


def send_notification(notification):
    logger.info('send_notification. notification = %s', notification)
    Group("notifications").send({'text': json.dumps(notification)})


@receiver(post_create_signal, sender=Post)
def post_create_signal_handler(sender, **kwargs):
    request = kwargs['request']
    instance = kwargs['instance']

    instance.created_by = request.user
    instance.save()

    send_notification({
        'type': 'created',
        'post': instance.name,
        'done_by': instance.created_by.username,
        'done_at': instance.created.strftime("%a %d %b %Y %H:%M"),
        })


@receiver(post_update_signal, sender=Post)
def post_update_signal_handler(sender, **kwargs):
    request = kwargs['request']
    instance = kwargs['instance']

    instance.updated_by = request.user
    instance.save()

    send_notification({
        'type': 'updated',
        'post': instance.name,
        'done_by': instance.updated_by.username,
        'done_at': instance.updated.strftime("%a %d %b %Y %H:%M"),
        })
