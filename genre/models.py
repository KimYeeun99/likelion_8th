from django.db import models

# Create your models here.
class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    title_genre = models.CharField(max_length=45, blank=True, null=True)
    content_genre = models.TextField()

    class Meta:
        managed = False
        db_table = 'genre'

    def __str__(self):
        return self.title_genre