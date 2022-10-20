from django.db import models



class task(models.Model):
    task=models.CharField(max_length=255)
    id=models.AutoField(primary_key=True)
