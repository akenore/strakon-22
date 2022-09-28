from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class FormationVideo(models.Model):

    CAT=[
        ('BIM', 'BIM'),
        ('TIPS', 'Astuse et conseils')
    ]
   
    post_date = models.DateTimeField(_("Publié"), auto_now_add=True)
    name = models.CharField(_("Titre"), max_length=250)
    slug = slug = AutoSlugField(
        populate_from='name', unique_with='name', unique=True)
    code = models.CharField(_("Code YouTube"), max_length=50)
    category= models.CharField('Choisir le catégorie', choices=CAT, max_length=10)
    

    class Meta:
        verbose_name = _("Formation Video")
        verbose_name_plural = _("Formation Videos")

    def __str__(self):
        return self.name