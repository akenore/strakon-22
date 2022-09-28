from django import forms
from django.utils.translation import gettext_lazy as _

from .models import (
    Blog,
    BlogCategories,
    Gallery,
    JourneeUtilisateur2022plus,
    PresentationFromYoutube,
    Video,
    Presentation,
    LicenceEtudiant,
    LicenceEtablissement,
    JourneeUtilisateur2021,
    FormationArmaturesCube,
    JourneeUtilisateur2022,
    JourneeUtilisateur2022plus,
    Batimat
)


class BlogCategoriesForm(forms.ModelForm):

    class Meta:
        model = BlogCategories
        fields = '__all__'


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author']
        widgets = {
            'category': forms.CheckboxSelectMultiple
        }
        labels = {
            'name': _("Titre d'article"),
            'view': _("Article"),
            'category': _("Choisissez une catégorie"),
            'image': _(""),
        }


class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = '__all__'


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = '__all__'
        widgets = {
            'language': forms.RadioSelect
        }


class PresentationForm(forms.ModelForm):

    class Meta:
        model = Presentation
        fields = '__all__'
        widgets = {
            'type_presentation': forms.RadioSelect
        }


class LicenceEtudiantForm(forms.ModelForm):

    class Meta:
        model = LicenceEtudiant
        fields = '__all__'
        widgets = {
            'commande': forms.RadioSelect
        }
        labels = {
            'certificat': _(""),
        }
        # help_texts = {
        #     'certificat': _('(uniquement fichier Pdf, jpg ou png de 2 Mo maximum)')
        # }
        # error_messages = {
        #     'certificat': {
        #         'max_length':_('on accept que fichier Pdf, jpg ou png'),
        #         }
        # }

    def __init__(self, *args, **kwargs):
        super(LicenceEtudiantForm, self).__init__(*args, **kwargs)
        self.fields['certificat'].label = ''
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'file-upload'

    def clean_confirm(self):
        confirm = self.cleaned_data.get('confirm')
        if not confirm:
            raise forms.ValidationError('Veuillez confirmer nos conditions')
        return confirm


class LicenceEtablissementForm(forms.ModelForm):

    class Meta:
        model = LicenceEtablissement
        fields = '__all__'
        widgets = {
            'commande': forms.RadioSelect
        }

    def clean_confirm(self):
        confirm = self.cleaned_data.get('confirm')
        if not confirm:
            raise forms.ValidationError('Veuillez confirmer nos conditions')
        return confirm


class JourneeUtilisateur2021Form(forms.ModelForm):

    class Meta:
        model = JourneeUtilisateur2021
        fields = '__all__'
        widgets = {
            'selected_date': forms.CheckboxSelectMultiple
        }
        labels = {
            'selected_date': _("Séléctionne une date (choix multiple possible)")
        }

    def clean(self, *args):
        try:
            JourneeUtilisateur2021.objects.get(
                email=self.cleaned_data['email'].lower())
            raise forms.ValidationError(
                {'email': "Vous êtes déjà inscrit dans la liste de la Journée d'utilisateur Strakon 2021"})
        except JourneeUtilisateur2021.DoesNotExist:
            pass
        return self.cleaned_data


class FormationArmaturesCubeForm(forms.ModelForm):

    class Meta:
        model = FormationArmaturesCube
        fields = '__all__'
        widgets = {
            'type_presentation': forms.RadioSelect
        }


class JourneeUtilisateur2022Form(forms.ModelForm):

    class Meta:
        model = JourneeUtilisateur2022
        fields = '__all__'

    # def clean(self, *args):
    #     try:
    #         JourneeUtilisateur2022.objects.get(email=self.cleaned_data['email'].lower())
    #         raise forms.ValidationError(
    #             {'email': "Vous êtes déjà inscrit dans la liste de la Journée d'utilisateur Strakon 2022"})
    #     except JourneeUtilisateur2022.DoesNotExist:
    #         pass
    #     return self.cleaned_data



class JourneeUtilisateur2022PlusForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(JourneeUtilisateur2022PlusForm, self).__init__(*args, **kwargs)
        self.fields['nom_de_societe'].widget.attrs.update({'placeholder': 'Société'})
        self.fields['contact'].widget.attrs.update({'placeholder': 'Nom et prénom'})
        self.fields['email'].widget.attrs.update({'placeholder': 'email@exemple.com'})
        self.fields['accompagnee'].widget.attrs.update({'placeholder': '+33 x xx xx xx xx'})
        

       

    class Meta:
        model = JourneeUtilisateur2022plus
        fields = '__all__'

class PresentationYoutuberForm(forms.ModelForm):

    class Meta:
        model = PresentationFromYoutube
        fields = '__all__'
        widgets = {
            'type_presentation': forms.RadioSelect
        }


class BatimatForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BatimatForm, self).__init__(*args, **kwargs)
        self.fields['subscriber_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['nom_ou_societe'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['code'].widget.attrs.update({'class': 'form-control'})
        self.fields['pays'].widget.attrs.update({'class': 'form-control'})
        self.fields['ville'].widget.attrs.update({'class': 'form-control'})
        

    class Meta:
        model = Batimat
        fields = '__all__'