import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Content(models.Model):
    content_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

