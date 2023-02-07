from django.db import models

class ScrapedData(models.Model):
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.TextField()
    keywords = models.TextField()

    def __str__(self):
        return self.title
