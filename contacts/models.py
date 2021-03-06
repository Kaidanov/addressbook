from django.db import models
from django.core.urlresolvers import reverse
# getting User from django auth to create owner of the contact
from django.contrib.auth.models import User


class Contact(models.Model):
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,

    )
    email = models.EmailField()
    owner = models.ForeignKey(User)  # User is django.contrib.auth.models

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name
        ])

    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk': self.id})
