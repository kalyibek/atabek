import os
from django.db import models
from django.conf import settings

class MedicalShows(models.Model):
    TYPE_IMG = (
        ('HEART', "HEART"),
        ('KIDNEYS', 'KIDNEYS'),
        ("LIVER", "LIVER"),
        ('EYES', 'EYES')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT))
    img_type = models.CharField(choices=TYPE_IMG, max_length=100)
    add_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
