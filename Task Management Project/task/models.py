from django.db import models
from datetime import datetime
from category.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField(CategoryModel)
    completed = models.BooleanField(default=False)
    assign_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.assign_date:
            self.assign_date = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    