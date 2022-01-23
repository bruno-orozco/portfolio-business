from django.db import models
from django.contrib.auth.models import User
import uuid
import os

class post(models.Model):
    """ Posts model """

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    text = models.TextField()

    def get_file_path(instance, filename):
        """ Function for valid is unique """

        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('photos/', filename)

    photo = models.ImageField(upload_to=get_file_path, null=True, blank=True,)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        
        return '{} by @{}'.format(self.title, self.author)