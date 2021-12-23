from django.db import models


class Project(models.Model):
    title = models.TextField(max_length=40)
    image = models.ImageField(upload_to='images/')
    details = models.TextField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.title
