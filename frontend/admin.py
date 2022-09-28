from django.contrib import admin
from .models import (
    BlogCategories,
    Blog,
    Video,
    Gallery,
    Presentation,
    LicenceEtudiant,
    LicenceEtablissement,
    JourneeUtilisateur2021,
    JourneeUtilisateur2022,
    JourneeUtilisateur2022plus,
    SelectDate,
    FormationArmaturesCube,
    PresentationFromYoutube,
    Batimat
)

admin.site.register(BlogCategories)
admin.site.register(Blog)
admin.site.register(Video)
admin.site.register(Gallery)
admin.site.register(Presentation)
admin.site.register(LicenceEtudiant)
admin.site.register(LicenceEtablissement)
admin.site.register(JourneeUtilisateur2021)
admin.site.register(JourneeUtilisateur2022)
admin.site.register(JourneeUtilisateur2022plus)
admin.site.register(SelectDate)
admin.site.register(FormationArmaturesCube)
admin.site.register(PresentationFromYoutube)
admin.site.register(Batimat)
