from django.db import models

# Create your models here.
class History(models.Model):
    id_history = models.AutoField(primary_key=True)
    title_history = models.CharField(max_length=45, blank=True, null=True)
    content_history = models.TextField()

    class Meta:
        managed = False
        db_table = 'history'

    def __str__(self):
        return self.title_history