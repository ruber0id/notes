from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=200)
    header = models.CharField(max_length=250)
    text = models.TextField()
    date_added = models.DateTimeField()
    reminder = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
