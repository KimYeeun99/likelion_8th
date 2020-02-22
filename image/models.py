from django.db import models

# Create your models here.
class Image(models.Model):
    id_image = models.AutoField(primary_key=True)
    file_image = models.TextField()
    name_image = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'image'

    def __str__(self):
        return self.name_image