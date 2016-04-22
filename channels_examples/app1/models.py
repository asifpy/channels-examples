from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(blank=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='%(class)ss_creators')
    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='%(class)ss_updators')

    def __unicode__(self):
        return self.name


class Vote(models.Model):
    item = models.CharField(
        max_length=50,
        choices=[
            ('banana', 'Banana'),
            ('chocolate', 'Chocolate'),
            ('lemon', 'Lemon')
        ]
        )

    number_of_votes = models.IntegerField(
        blank=True,
        null=True,
        default=0)
