from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader import fields

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=30)
    contenu = RichTextUploadingField()
    image = fields.widgets.CKEditorUploadingWidget()
    categorie=models.ForeignKey('Categorie', on_delete=models.CASCADE, blank=True, default=1)

    class Meta:
        verbose_name="article"
        ordering = ['titre']

    def __str__(self):
        return self.titre

class Categorie(models.Model):
    nom=models.CharField(max_length=30)

    class Meta:
        verbose_name='categorie'
        ordering=['nom']

    def __str__(self):
        return self.nom
