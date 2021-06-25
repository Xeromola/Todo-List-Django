from django.db import models

# Create your models here.
class todo_item(models.Model):
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    