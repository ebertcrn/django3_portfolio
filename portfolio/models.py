from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)    # Django Model Fields: https://docs.djangoproject.com/en/3.1/topics/db/models/
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)   # blank = True: url is optional

    def __str__(self):
        return self.title   # changes the project name to the specific title