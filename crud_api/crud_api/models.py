from django.db import models

class CrudAPI(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title + ': ' + self.sub_title