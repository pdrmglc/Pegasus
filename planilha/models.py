from django.db import models

# Create your models here.

class Planilha(models.Model):
    arquivo = models.FileField(upload_to='planilhas/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.arquivo.name