from django.db import models
from django.conf import settings

# Create your models here.

class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

 # 'links.Link': In this case, it's referring to the Link model in the links app.
class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.ForeignKey('links.Link', related_name='votes', on_delete=models.CASCADE)

