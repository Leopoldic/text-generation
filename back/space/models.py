from django.db import models
from django_pandas.managers import DataFrameManager
from datetime import datetime,date
from django.utils import timezone

class result(models.Model):
    generate_text = models.CharField(max_length=10000)
    bleu = models.IntegerField()
    term_text = models.ForeignKey('use_text',on_delete=models.CASCADE,)
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return (str(self.date))


class use_text(models.Model):
    text = models.CharField(max_length=10000)