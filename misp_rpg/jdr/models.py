from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=30)
    contenu = models.TextField(null=True)

    class Meta:
        verbose_name="article"
        ordering = ['titre']

    def __str__(self):
        return self.titre