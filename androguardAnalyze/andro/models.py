from django.db import models


class Document(models.Model):
    apk = models.FileField(upload_to='apks/')

