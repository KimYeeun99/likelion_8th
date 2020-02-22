from django.db import models

# Create your models here.
class Dictionary(models.Model):
    id_dict = models.AutoField(primary_key=True)
    title_dict = models.CharField(max_length=100, blank=True, null=True)
    alpha = models.CharField(max_length=2, blank=True, null=True)
    content_dict = models.TextField()

    class Meta:
        managed = False
        db_table = 'dictionary'

    def __str__(self):
        return self.title_dict