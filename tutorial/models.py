from django.db import models
from django.core.urlresolvers import reverse


class People(models.Model):
    name = models.CharField(max_length=32, default="p1")

    def get_absolute_url(self):
        return "people/%s/" % self.id
