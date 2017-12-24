from django.db import models

# Create your models here.


class TimeLine(models.Model):
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'timeline'
