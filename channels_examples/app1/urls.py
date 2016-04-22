from django.conf.urls import url
from django.views.generic import TemplateView

from app1.views import votes

urlpatterns = [
    url(
        r'^votes/$',
        votes,
        name='app1-votes'),
]
