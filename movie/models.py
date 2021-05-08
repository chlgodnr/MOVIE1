from django.db import models

class Current(models.Model):
    current_title = models.CharField(max_length=100)
    current_poster = models.TextField() #fileField

    def __str__(self):
        return self.current_title
