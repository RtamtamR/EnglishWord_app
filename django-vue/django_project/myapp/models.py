from django.db import models

# Create your models here.
class Dictionary(models.Model):
    vocabindex = models.IntegerField(db_column='vocabIndex', primary_key=True)  # Field name made lowercase.
    vocab = models.CharField(max_length=40)
    pronounce = models.CharField(max_length=40)
    meaning = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dictionary'