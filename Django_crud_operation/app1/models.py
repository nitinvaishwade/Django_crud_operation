from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime


class people_detail(models.Model):

    """
    people details.
    """
    # Values for the risk choices
    
    username = models.CharField(unique=True, max_length=50)
    fullname = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=32, blank=True)
    state = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=32, blank=True)
    start_date = models.DateTimeField(
        default=datetime.datetime.now(), null=True, blank=True
    )
