from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import City, Region, Country
class BlogCategories(models.Model):

    post_date = models.DateTimeField(_("Publié"), auto_now_add=True)
    name = models.CharField(_("Nom"), max_length=50)
    slug = AutoSlugField(populate_from='name', unique_with='name', unique=True)

    class Meta:
        verbose_name = _("Blog Categories")
        verbose_name_plural = _("Blog Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BlogCategories_detail", kwargs={"pk": self.pk})


class Blog(models.Model):
    post_date = models.DateTimeField(_("Publié"), auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(
        BlogCategories, verbose_name=_("Category"))
    name = models.CharField(_("Nom"), max_length=250)
    slug = AutoSlugField(populate_from='name', unique_with='name', unique=True)
    image = models.ImageField(
        _("Image principale"), upload_to='blog/%Y/%m/%d/', default='default.jpg')
    view = RichTextUploadingField()

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Blog_detail", kwargs={"slug": self.slug})


class Video(models.Model):
    LNG = [
        ('FR', 'FR'),
        ('EN', 'EN'),
        ('DE', 'DE')
    ]
    post_date = models.DateTimeField(_("Publié"), auto_now_add=True)
    name = models.CharField(_("Titre"), max_length=250)
    slug = slug = AutoSlugField(
        populate_from='name', unique_with='name', unique=True)
    code = models.CharField(_("Code YouTube"), max_length=50)
    image = models.ImageField(_("Image principale"),
                              upload_to='video/%Y/%m/%d/', default='default.jpg')
    language = models.CharField(
        _("Langue de la vidéo"), choices=LNG, max_length=50, default='FR')

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Video_detail", kwargs={"slug": self.slug})


class Gallery(models.Model):
    post_date = models.DateTimeField(_("Publié"), auto_now_add=True)
    name = models.CharField(_("Titre"), max_length=250)
    slug = slug = AutoSlugField(
        populate_from='name', unique_with='name', unique=True)
    image = models.ImageField(
        _("Image"), upload_to='gallery/%Y/%m/%d/', default='default.jpg')

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Gallery_detail", kwargs={"slug": self.slug})


class Presentation(models.Model):
    PRESENTATION = [
        ('sur place', 'Présentation du logiciel de CAO STRAKON sur place'),
        ('via internet', 'Présentation du logiciel de CAO STRAKON via Internet')
    ]
    BRANCH = [

        ('Ingénieur structurale', 'Ingénieur structurale'),
        ('Construction préfabriquée', 'Construction préfabriquée'),
        ('Architecture', 'Architecture'),
        ("Commerce de l'acier", "Commerce de l'acier"),
        ("Établissements d'enseignement", "Établissements d'enseignement"),
        ('Étudiant', 'Étudiant'),
        ('Autres', 'Autres')

    ]
    COUNTRIES = [
        ('Algérie', 'Algérie'),
        ('Afrique du Sud', 'Afrique du Sud'),
        ('Angola', 'Angola'),
        ('Bénin', 'Bénin'),
        ('Botswana', 'Botswana'),
        ('Burkina', 'Burkina'),
        ('Burundi', 'Burundi'),
        ('Cameroun', 'Cameroun'),
        ('Cap-Vert', 'Cap-Vert'),
        ('République centrafricaine', 'République centrafricaine'),
        ('Comores', 'Comores'),
        ('Congo', 'Congo'),
        ('République démocratique du Congo', 'République démocratique du Congo'),
        ("Côte d'Ivoire", "Côte d'Ivoire"),
        ('Djibouti', 'Djibouti'),
        ('Égypte', 'Égypte'),
        ('Érythrée', 'Érythrée'),
        ('Éthiopie', 'Éthiopie'),
        ('Gabon', 'Gabon'),
        ('Gambie', 'Gambie'),
        ('Ghana', 'Ghana'),
        ('Guinée', 'Guinée'),
        ('Guinée-Bissau', 'Guinée-Bissau'),
        ('Guinée équatoriale', 'Guinée équatoriale'),
        ('Kenya', 'Kenya'),
        ('Lesotho', 'Lesotho'),
        ('Libéria', 'Libéria'),
        ('Libye', 'Libye'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Mali', 'Mali'),
        ('Maroc', 'Maroc'),
        ('Maurice', 'Maurice'),
        ('Mauritanie', 'Mauritanie'),
        ('Mozambique', 'Mozambique'),
        ('Namibie', 'Namibie'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Ouganda', 'Ouganda'),
        ('Rwanda', 'Rwanda'),
        ('Sao Tomé-et-Principe', 'Sao Tomé-et-Principe'),
        ('Sénégal', 'Sénégal'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Somalie', 'Somalie'),
        ('Soudan', 'Soudan'),
        ('Sud-Soudan', 'Sud-Soudan'),
        ('Swaziland', 'Swaziland'),
        ('Tanzanie', 'Tanzanie'),
        ('Tchad', 'Tchad'),
        ('Togo', 'Togo'),
        ('Tunisie', 'Tunisie'),
        ('Zambie', 'Zambie'),
        ('Zimbabwe', 'Zimbabwe'),
        ('Antigua-et-Barbuda', 'Antigua-et-Barbuda'),
        ('Argentine', 'Argentine'),
        ('Bahamas', 'Bahamas'),
        ('Barbade', 'Barbade'),
        ('Belize', 'Belize'),
        ('Bolivie', 'Bolivie'),
        ('Brésil', 'Brésil'),
        ('Canada', 'Canada'),
        ('Chili', 'Chili'),
        ('Colombie', 'Colombie'),
        ('Costa Rica', 'Costa Rica'),
        ('Cuba', 'Cuba'),
        ('République dominicaine', 'République dominicaine'),
        ('Dominique', 'Dominique'),
        ('Équateur', 'Équateur'),
        ('États-Unis', 'États-Unis'),
        ('Grenade', 'Grenade'),
        ('Guatemala', 'Guatemala'),
        ('Guyana', 'Guyana'),
        ('Haïti', 'Haïti'),
        ('Honduras', 'Honduras'),
        ('Jamaïque', 'Jamaïque'),
        ('Mexique', 'Mexique'),
        ('Nicaragua', 'Nicaragua'),
        ('Panama', 'Panama'),
        ('Paraguay', 'Paraguay'),
        ('Pérou', 'Pérou'),
        ('Porto Rico', 'Porto Rico'),
        ('Saint-Christophe-et-Niévès', 'Saint-Christophe-et-Niévès'),
        ('Sainte-Lucie', 'Sainte-Lucie'),
        ('Saint-Vincent-et-les Grenadines', 'Saint-Vincent-et-les Grenadines'),
        ('Salvador', 'Salvador'),
        ('Suriname', 'Suriname'),
        ('Trinité-et-Tobago', 'Trinité-et-Tobago'),
        ('Uruguay', 'Uruguay'),
        ('Venezuela', 'Venezuela'),
        ('Afghanistan', 'Afghanistan'),
        ('Arabie saoudite', 'Arabie saoudite'),
        ('Bahreïn', 'Bahreïn'),
        ('Bangladesh', 'Bangladesh'),
        ('Bhoutan', 'Bhoutan'),
        ('Birmanie', 'Birmanie'),
        ('Brunei', 'Brunei'),
        ('Cambodge', 'Cambodge'),
        ('Chine', 'Chine'),
        ('Corée du Nord', 'Corée du Nord'),
        ('Corée du Sud', 'Corée du Sud'),
        ('Émirats arabes unis', 'Émirats arabes unis'),
        ('Inde', 'Inde'),
        ('Indonésie', 'Indonésie'),
        ('Irak', 'Irak'),
        ('Iran', 'Iran'),
        ('Palestine', 'Palestine'),
        ('Japon', 'Japon'),
        ('Jordanie', 'Jordanie'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kirghizistan', 'Kirghizistan'),
        ('Koweït', 'Koweït'),
        ('Laos', 'Laos'),
        ('Liban', 'Liban'),
        ('Malaisie', 'Malaisie'),
        ('Maldives', 'Maldives'),
        ('Mongolie', 'Mongolie'),
        ('Népal', 'Népal'),
        ('Oman', 'Oman'),
        ('Ouzbékistan', 'Ouzbékistan'),
        ('Pakistan', 'Pakistan'),
        ('Philippines', 'Philippines'),
        ('Qatar', 'Qatar'),
        ('Singapour', 'Singapour'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Syrie', 'Syrie'),
        ('Tadjikistan', 'Tadjikistan'),
        ('Taïwan', 'Taïwan'),
        ('Thaïlande', 'Thaïlande'),
        ('Timor oriental', 'Timor oriental'),
        ('Turkménistan', 'Turkménistan'),
        ('Turquie', 'Turquie'),
        ('Viêt Nam', 'Viêt Nam'),
        ('Yémen', 'Yémen'),
        ('Allemagne', 'Allemagne'),
        ('Albanie', 'Albanie'),
        ('Andorre', 'Andorre'),
        ('Arménie', 'Arménie'),
        ('Autriche', 'Autriche'),
        ('Azerbaïdjan', 'Azerbaïdjan'),
        ('Belgique', 'Belgique'),
        ('Biélorussie', 'Biélorussie'),
        ('Bosnie-Herzégovine', 'Bosnie-Herzégovine'),
        ('Bulgarie', 'Bulgarie'),
        ('Chypre', 'Chypre'),
        ('Croatie', 'Croatie'),
        ('Danemark', 'Danemark'),
        ('Espagne', 'Espagne'),
        ('Estonie', 'Estonie'),
        ('Finlande', 'Finlande'),
        ('France', 'France'),
        ('Géorgie', 'Géorgie'),
        ('Grèce', 'Grèce'),
        ('Hongrie', 'Hongrie'),
        ('Irlande', 'Irlande'),
        ('Islande', 'Islande'),
        ('Italie', 'Italie'),
        ('Lettonie', 'Lettonie'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lituanie', 'Lituanie'),
        ('Luxembourg', 'Luxembourg'),
        ('République de Macédoine', 'République de Macédoine'),
        ('Malte', 'Malte'),
        ('Moldavie', 'Moldavie'),
        ('Monaco', 'Monaco'),
        ('Monténégro', 'Monténégro'),
        ('Norvège', 'Norvège'),
        ('Pays-Bas', 'Pays-Bas'),
        ('Pologne', 'Pologne'),
        ('Portugal', 'Portugal'),
        ('République tchèque', 'République tchèque'),
        ('Roumanie', 'Roumanie'),
        ('Royaume-Uni', 'Royaume-Uni'),
        ('Russie', 'Russie'),
        ('Saint-Marin', 'Saint-Marin'),
        ('Serbie', 'Serbie'),
        ('Slovaquie', 'Slovaquie'),
        ('Slovénie', 'Slovénie'),
        ('Suède', 'Suède'),
        ('Suisse', 'Suisse'),
        ('Ukraine', 'Ukraine'),
        ('Vatican', 'Vatican'),
        ('Australie', 'Australie'),
        ('Fidji', 'Fidji'),
        ('Kiribati', 'Kiribati'),
        ('Marshall', 'Marshall'),
        ('Micronésie', 'Micronésie'),
        ('Nauru', 'Nauru'),
        ('Nouvelle-Zélande', 'Nouvelle-Zélande'),
        ('Palaos', 'Palaos'),
        ('Papouasie-Nouvelle-Guinée', 'Papouasie-Nouvelle-Guinée'),
        ('Salomon', 'Salomon'),
        ('Samoa', 'Samoa'),
        ('Tonga', 'Tonga'),
        ('Tuvalu', 'Tuvalu'),
        ('Vanuatu', 'Vanuatu'),
    ]
    post_date = models.DateTimeField(_("Publié"), auto_now_add=True)
    slug = slug = AutoSlugField(
        populate_from='societe', unique_with='societe', unique=True)
    type_presentation = models.CharField(
        _("Type de présentation"), choices=PRESENTATION, max_length=50, default='via internet')

    branche = models.CharField(_("Branche"), choices=BRANCH, max_length=50)
    societe = models.CharField(_("Société"), max_length=50)
    contact = models.CharField(_("Contact"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    tel = models.CharField(_("Téléphone"), max_length=50)
    address = models.CharField(_("Adresse"), max_length=50)
    code_postal = models.CharField(_("Code Postal"), max_length=50)
    pays = models.CharField(_("Pays"), choices=COUNTRIES, max_length=50)

    class Meta:
        verbose_name = _("Presentation")
        verbose_name_plural = _("Presentations")

    def __str__(self):
        return self.societe

    def get_absolute_url(self):
        return reverse("presentation_detail", kwargs={"pk": self.pk})


class LicenceEtudiant(models.Model):
    COMANDE = [
        ('Licence', 'Licence'),
        ('Mise à jour', 'Mise à jour')
    ]
    COUNTRIES = [
        ('Algérie', 'Algérie'),
        ('Afrique du Sud', 'Afrique du Sud'),
        ('Angola', 'Angola'),
        ('Bénin', 'Bénin'),
        ('Botswana', 'Botswana'),
        ('Burkina', 'Burkina'),
        ('Burundi', 'Burundi'),
        ('Cameroun', 'Cameroun'),
        ('Cap-Vert', 'Cap-Vert'),
        ('République centrafricaine', 'République centrafricaine'),
        ('Comores', 'Comores'),
        ('Congo', 'Congo'),
        ('République démocratique du Congo', 'République démocratique du Congo'),
        ("Côte d'Ivoire", "Côte d'Ivoire"),
        ('Djibouti', 'Djibouti'),
        ('Égypte', 'Égypte'),
        ('Érythrée', 'Érythrée'),
        ('Éthiopie', 'Éthiopie'),
        ('Gabon', 'Gabon'),
        ('Gambie', 'Gambie'),
        ('Ghana', 'Ghana'),
        ('Guinée', 'Guinée'),
        ('Guinée-Bissau', 'Guinée-Bissau'),
        ('Guinée équatoriale', 'Guinée équatoriale'),
        ('Kenya', 'Kenya'),
        ('Lesotho', 'Lesotho'),
        ('Libéria', 'Libéria'),
        ('Libye', 'Libye'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Mali', 'Mali'),
        ('Maroc', 'Maroc'),
        ('Maurice', 'Maurice'),
        ('Mauritanie', 'Mauritanie'),
        ('Mozambique', 'Mozambique'),
        ('Namibie', 'Namibie'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Ouganda', 'Ouganda'),
        ('Rwanda', 'Rwanda'),
        ('Sao Tomé-et-Principe', 'Sao Tomé-et-Principe'),
        ('Sénégal', 'Sénégal'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Somalie', 'Somalie'),
        ('Soudan', 'Soudan'),
        ('Sud-Soudan', 'Sud-Soudan'),
        ('Swaziland', 'Swaziland'),
        ('Tanzanie', 'Tanzanie'),
        ('Tchad', 'Tchad'),
        ('Togo', 'Togo'),
        ('Tunisie', 'Tunisie'),
        ('Zambie', 'Zambie'),
        ('Zimbabwe', 'Zimbabwe'),
        ('Antigua-et-Barbuda', 'Antigua-et-Barbuda'),
        ('Argentine', 'Argentine'),
        ('Bahamas', 'Bahamas'),
        ('Barbade', 'Barbade'),
        ('Belize', 'Belize'),
        ('Bolivie', 'Bolivie'),
        ('Brésil', 'Brésil'),
        ('Canada', 'Canada'),
        ('Chili', 'Chili'),
        ('Colombie', 'Colombie'),
        ('Costa Rica', 'Costa Rica'),
        ('Cuba', 'Cuba'),
        ('République dominicaine', 'République dominicaine'),
        ('Dominique', 'Dominique'),
        ('Équateur', 'Équateur'),
        ('États-Unis', 'États-Unis'),
        ('Grenade', 'Grenade'),
        ('Guatemala', 'Guatemala'),
        ('Guyana', 'Guyana'),
        ('Haïti', 'Haïti'),
        ('Honduras', 'Honduras'),
        ('Jamaïque', 'Jamaïque'),
        ('Mexique', 'Mexique'),
        ('Nicaragua', 'Nicaragua'),
        ('Panama', 'Panama'),
        ('Paraguay', 'Paraguay'),
        ('Pérou', 'Pérou'),
        ('Porto Rico', 'Porto Rico'),
        ('Saint-Christophe-et-Niévès', 'Saint-Christophe-et-Niévès'),
        ('Sainte-Lucie', 'Sainte-Lucie'),
        ('Saint-Vincent-et-les Grenadines', 'Saint-Vincent-et-les Grenadines'),
        ('Salvador', 'Salvador'),
        ('Suriname', 'Suriname'),
        ('Trinité-et-Tobago', 'Trinité-et-Tobago'),
        ('Uruguay', 'Uruguay'),
        ('Venezuela', 'Venezuela'),
        ('Afghanistan', 'Afghanistan'),
        ('Arabie saoudite', 'Arabie saoudite'),
        ('Bahreïn', 'Bahreïn'),
        ('Bangladesh', 'Bangladesh'),
        ('Bhoutan', 'Bhoutan'),
        ('Birmanie', 'Birmanie'),
        ('Brunei', 'Brunei'),
        ('Cambodge', 'Cambodge'),
        ('Chine', 'Chine'),
        ('Corée du Nord', 'Corée du Nord'),
        ('Corée du Sud', 'Corée du Sud'),
        ('Émirats arabes unis', 'Émirats arabes unis'),
        ('Inde', 'Inde'),
        ('Indonésie', 'Indonésie'),
        ('Irak', 'Irak'),
        ('Iran', 'Iran'),
        ('Palestine', 'Palestine'),
        ('Japon', 'Japon'),
        ('Jordanie', 'Jordanie'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kirghizistan', 'Kirghizistan'),
        ('Koweït', 'Koweït'),
        ('Laos', 'Laos'),
        ('Liban', 'Liban'),
        ('Malaisie', 'Malaisie'),
        ('Maldives', 'Maldives'),
        ('Mongolie', 'Mongolie'),
        ('Népal', 'Népal'),
        ('Oman', 'Oman'),
        ('Ouzbékistan', 'Ouzbékistan'),
        ('Pakistan', 'Pakistan'),
        ('Philippines', 'Philippines'),
        ('Qatar', 'Qatar'),
        ('Singapour', 'Singapour'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Syrie', 'Syrie'),
        ('Tadjikistan', 'Tadjikistan'),
        ('Taïwan', 'Taïwan'),
        ('Thaïlande', 'Thaïlande'),
        ('Timor oriental', 'Timor oriental'),
        ('Turkménistan', 'Turkménistan'),
        ('Turquie', 'Turquie'),
        ('Viêt Nam', 'Viêt Nam'),
        ('Yémen', 'Yémen'),
        ('Allemagne', 'Allemagne'),
        ('Albanie', 'Albanie'),
        ('Andorre', 'Andorre'),
        ('Arménie', 'Arménie'),
        ('Autriche', 'Autriche'),
        ('Azerbaïdjan', 'Azerbaïdjan'),
        ('Belgique', 'Belgique'),
        ('Biélorussie', 'Biélorussie'),
        ('Bosnie-Herzégovine', 'Bosnie-Herzégovine'),
        ('Bulgarie', 'Bulgarie'),
        ('Chypre', 'Chypre'),
        ('Croatie', 'Croatie'),
        ('Danemark', 'Danemark'),
        ('Espagne', 'Espagne'),
        ('Estonie', 'Estonie'),
        ('Finlande', 'Finlande'),
        ('France', 'France'),
        ('Géorgie', 'Géorgie'),
        ('Grèce', 'Grèce'),
        ('Hongrie', 'Hongrie'),
        ('Irlande', 'Irlande'),
        ('Islande', 'Islande'),
        ('Italie', 'Italie'),
        ('Lettonie', 'Lettonie'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lituanie', 'Lituanie'),
        ('Luxembourg', 'Luxembourg'),
        ('République de Macédoine', 'République de Macédoine'),
        ('Malte', 'Malte'),
        ('Moldavie', 'Moldavie'),
        ('Monaco', 'Monaco'),
        ('Monténégro', 'Monténégro'),
        ('Norvège', 'Norvège'),
        ('Pays-Bas', 'Pays-Bas'),
        ('Pologne', 'Pologne'),
        ('Portugal', 'Portugal'),
        ('République tchèque', 'République tchèque'),
        ('Roumanie', 'Roumanie'),
        ('Royaume-Uni', 'Royaume-Uni'),
        ('Russie', 'Russie'),
        ('Saint-Marin', 'Saint-Marin'),
        ('Serbie', 'Serbie'),
        ('Slovaquie', 'Slovaquie'),
        ('Slovénie', 'Slovénie'),
        ('Suède', 'Suède'),
        ('Suisse', 'Suisse'),
        ('Ukraine', 'Ukraine'),
        ('Vatican', 'Vatican'),
        ('Australie', 'Australie'),
        ('Fidji', 'Fidji'),
        ('Kiribati', 'Kiribati'),
        ('Marshall', 'Marshall'),
        ('Micronésie', 'Micronésie'),
        ('Nauru', 'Nauru'),
        ('Nouvelle-Zélande', 'Nouvelle-Zélande'),
        ('Palaos', 'Palaos'),
        ('Papouasie-Nouvelle-Guinée', 'Papouasie-Nouvelle-Guinée'),
        ('Salomon', 'Salomon'),
        ('Samoa', 'Samoa'),
        ('Tonga', 'Tonga'),
        ('Tuvalu', 'Tuvalu'),
        ('Vanuatu', 'Vanuatu'),
    ]
    post_date = models.DateTimeField(_("Publié"), auto_now_add=True)
    slug = slug = AutoSlugField(
        populate_from='name', unique_with='name', unique=True)
    commande = models.CharField(
        _("Commandez"), choices=COMANDE, max_length=50, default='Licence')
    name = models.CharField(_("Votre nom"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    address = models.CharField(_("Adresse"), max_length=50)
    code_postal = models.CharField(_("Code Postal"), max_length=50)
    pays = models.CharField(_("Pays"), choices=COUNTRIES, max_length=50)
    enseignement = models.CharField(
        _("Enseignement secondaire / professionnelle"), max_length=200)
    ecole = models.CharField(_("École / Lieu"), max_length=200)
    etude = models.CharField(
        _("Étude / fin de formation estimée"), max_length=200)
    telephone = models.CharField(_("Téléphone"), max_length=50)
    certificat = models.FileField(
        _("Certificat d'immatriculation ou téléchargement similaire"), upload_to='etudian/%Y/%m/%d/', max_length=100)
    confirm = models.BooleanField(
        _("Confirmer les conditions d'utilisation de la licence étudiant"))

    class Meta:
        verbose_name = _("Licence Etudiant")
        verbose_name_plural = _("Licence Etudiants")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("licence_etudiant_detail", kwargs={"pk": self.pk})


class LicenceEtablissement(models.Model):
    COMANDE = [
        ('Licence', 'Licence'),
        ('Mise à jour', 'Mise à jour')
    ]
    COUNTRIES = [
        ('Algérie', 'Algérie'),
        ('Afrique du Sud', 'Afrique du Sud'),
        ('Angola', 'Angola'),
        ('Bénin', 'Bénin'),
        ('Botswana', 'Botswana'),
        ('Burkina', 'Burkina'),
        ('Burundi', 'Burundi'),
        ('Cameroun', 'Cameroun'),
        ('Cap-Vert', 'Cap-Vert'),
        ('République centrafricaine', 'République centrafricaine'),
        ('Comores', 'Comores'),
        ('Congo', 'Congo'),
        ('République démocratique du Congo', 'République démocratique du Congo'),
        ("Côte d'Ivoire", "Côte d'Ivoire"),
        ('Djibouti', 'Djibouti'),
        ('Égypte', 'Égypte'),
        ('Érythrée', 'Érythrée'),
        ('Éthiopie', 'Éthiopie'),
        ('Gabon', 'Gabon'),
        ('Gambie', 'Gambie'),
        ('Ghana', 'Ghana'),
        ('Guinée', 'Guinée'),
        ('Guinée-Bissau', 'Guinée-Bissau'),
        ('Guinée équatoriale', 'Guinée équatoriale'),
        ('Kenya', 'Kenya'),
        ('Lesotho', 'Lesotho'),
        ('Libéria', 'Libéria'),
        ('Libye', 'Libye'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Mali', 'Mali'),
        ('Maroc', 'Maroc'),
        ('Maurice', 'Maurice'),
        ('Mauritanie', 'Mauritanie'),
        ('Mozambique', 'Mozambique'),
        ('Namibie', 'Namibie'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Ouganda', 'Ouganda'),
        ('Rwanda', 'Rwanda'),
        ('Sao Tomé-et-Principe', 'Sao Tomé-et-Principe'),
        ('Sénégal', 'Sénégal'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Somalie', 'Somalie'),
        ('Soudan', 'Soudan'),
        ('Sud-Soudan', 'Sud-Soudan'),
        ('Swaziland', 'Swaziland'),
        ('Tanzanie', 'Tanzanie'),
        ('Tchad', 'Tchad'),
        ('Togo', 'Togo'),
        ('Tunisie', 'Tunisie'),
        ('Zambie', 'Zambie'),
        ('Zimbabwe', 'Zimbabwe'),
        ('Antigua-et-Barbuda', 'Antigua-et-Barbuda'),
        ('Argentine', 'Argentine'),
        ('Bahamas', 'Bahamas'),
        ('Barbade', 'Barbade'),
        ('Belize', 'Belize'),
        ('Bolivie', 'Bolivie'),
        ('Brésil', 'Brésil'),
        ('Canada', 'Canada'),
        ('Chili', 'Chili'),
        ('Colombie', 'Colombie'),
        ('Costa Rica', 'Costa Rica'),
        ('Cuba', 'Cuba'),
        ('République dominicaine', 'République dominicaine'),
        ('Dominique', 'Dominique'),
        ('Équateur', 'Équateur'),
        ('États-Unis', 'États-Unis'),
        ('Grenade', 'Grenade'),
        ('Guatemala', 'Guatemala'),
        ('Guyana', 'Guyana'),
        ('Haïti', 'Haïti'),
        ('Honduras', 'Honduras'),
        ('Jamaïque', 'Jamaïque'),
        ('Mexique', 'Mexique'),
        ('Nicaragua', 'Nicaragua'),
        ('Panama', 'Panama'),
        ('Paraguay', 'Paraguay'),
        ('Pérou', 'Pérou'),
        ('Porto Rico', 'Porto Rico'),
        ('Saint-Christophe-et-Niévès', 'Saint-Christophe-et-Niévès'),
        ('Sainte-Lucie', 'Sainte-Lucie'),
        ('Saint-Vincent-et-les Grenadines', 'Saint-Vincent-et-les Grenadines'),
        ('Salvador', 'Salvador'),
        ('Suriname', 'Suriname'),
        ('Trinité-et-Tobago', 'Trinité-et-Tobago'),
        ('Uruguay', 'Uruguay'),
        ('Venezuela', 'Venezuela'),
        ('Afghanistan', 'Afghanistan'),
        ('Arabie saoudite', 'Arabie saoudite'),
        ('Bahreïn', 'Bahreïn'),
        ('Bangladesh', 'Bangladesh'),
        ('Bhoutan', 'Bhoutan'),
        ('Birmanie', 'Birmanie'),
        ('Brunei', 'Brunei'),
        ('Cambodge', 'Cambodge'),
        ('Chine', 'Chine'),
        ('Corée du Nord', 'Corée du Nord'),
        ('Corée du Sud', 'Corée du Sud'),
        ('Émirats arabes unis', 'Émirats arabes unis'),
        ('Inde', 'Inde'),
        ('Indonésie', 'Indonésie'),
        ('Irak', 'Irak'),
        ('Iran', 'Iran'),
        ('Palestine', 'Palestine'),
        ('Japon', 'Japon'),
        ('Jordanie', 'Jordanie'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kirghizistan', 'Kirghizistan'),
        ('Koweït', 'Koweït'),
        ('Laos', 'Laos'),
        ('Liban', 'Liban'),
        ('Malaisie', 'Malaisie'),
        ('Maldives', 'Maldives'),
        ('Mongolie', 'Mongolie'),
        ('Népal', 'Népal'),
        ('Oman', 'Oman'),
        ('Ouzbékistan', 'Ouzbékistan'),
        ('Pakistan', 'Pakistan'),
        ('Philippines', 'Philippines'),
        ('Qatar', 'Qatar'),
        ('Singapour', 'Singapour'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Syrie', 'Syrie'),
        ('Tadjikistan', 'Tadjikistan'),
        ('Taïwan', 'Taïwan'),
        ('Thaïlande', 'Thaïlande'),
        ('Timor oriental', 'Timor oriental'),
        ('Turkménistan', 'Turkménistan'),
        ('Turquie', 'Turquie'),
        ('Viêt Nam', 'Viêt Nam'),
        ('Yémen', 'Yémen'),
        ('Allemagne', 'Allemagne'),
        ('Albanie', 'Albanie'),
        ('Andorre', 'Andorre'),
        ('Arménie', 'Arménie'),
        ('Autriche', 'Autriche'),
        ('Azerbaïdjan', 'Azerbaïdjan'),
        ('Belgique', 'Belgique'),
        ('Biélorussie', 'Biélorussie'),
        ('Bosnie-Herzégovine', 'Bosnie-Herzégovine'),
        ('Bulgarie', 'Bulgarie'),
        ('Chypre', 'Chypre'),
        ('Croatie', 'Croatie'),
        ('Danemark', 'Danemark'),
        ('Espagne', 'Espagne'),
        ('Estonie', 'Estonie'),
        ('Finlande', 'Finlande'),
        ('France', 'France'),
        ('Géorgie', 'Géorgie'),
        ('Grèce', 'Grèce'),
        ('Hongrie', 'Hongrie'),
        ('Irlande', 'Irlande'),
        ('Islande', 'Islande'),
        ('Italie', 'Italie'),
        ('Lettonie', 'Lettonie'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lituanie', 'Lituanie'),
        ('Luxembourg', 'Luxembourg'),
        ('République de Macédoine', 'République de Macédoine'),
        ('Malte', 'Malte'),
        ('Moldavie', 'Moldavie'),
        ('Monaco', 'Monaco'),
        ('Monténégro', 'Monténégro'),
        ('Norvège', 'Norvège'),
        ('Pays-Bas', 'Pays-Bas'),
        ('Pologne', 'Pologne'),
        ('Portugal', 'Portugal'),
        ('République tchèque', 'République tchèque'),
        ('Roumanie', 'Roumanie'),
        ('Royaume-Uni', 'Royaume-Uni'),
        ('Russie', 'Russie'),
        ('Saint-Marin', 'Saint-Marin'),
        ('Serbie', 'Serbie'),
        ('Slovaquie', 'Slovaquie'),
        ('Slovénie', 'Slovénie'),
        ('Suède', 'Suède'),
        ('Suisse', 'Suisse'),
        ('Ukraine', 'Ukraine'),
        ('Vatican', 'Vatican'),
        ('Australie', 'Australie'),
        ('Fidji', 'Fidji'),
        ('Kiribati', 'Kiribati'),
        ('Marshall', 'Marshall'),
        ('Micronésie', 'Micronésie'),
        ('Nauru', 'Nauru'),
        ('Nouvelle-Zélande', 'Nouvelle-Zélande'),
        ('Palaos', 'Palaos'),
        ('Papouasie-Nouvelle-Guinée', 'Papouasie-Nouvelle-Guinée'),
        ('Salomon', 'Salomon'),
        ('Samoa', 'Samoa'),
        ('Tonga', 'Tonga'),
        ('Tuvalu', 'Tuvalu'),
        ('Vanuatu', 'Vanuatu'),
    ]
    post_date = models.DateTimeField(_("Publié"), auto_now_add=True)
    slug = slug = AutoSlugField(
        populate_from='name', unique_with='name', unique=True)
    commande = models.CharField(
        _("Commandez"), choices=COMANDE, max_length=50, default='Licence')
    name = models.CharField(_("Personne de contact"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    telephone = models.CharField(_("Téléphone"), max_length=50)
    address = models.CharField(_("Adresse"), max_length=50)
    code_postal = models.CharField(_("Code Postal"), max_length=50)
    pays = models.CharField(_("Pays"), choices=COUNTRIES, max_length=50)
    domaine = models.CharField(_("Domaine"), max_length=50)
    confirm = models.BooleanField(
        _("Confirmer les conditions d'utilisation de la licence étudiant"))

    class Meta:
        verbose_name = _("Licence Etablissement")
        verbose_name_plural = _("Licence Etablissements")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("licence_etablissement_detail", kwargs={"pk": self.pk})


class SelectDate(models.Model):

    day_num = models.IntegerField(_("Ajouter Date de jour"))

    def __str__(self):
        return (f"Le jour: {self.day_num}/06")

    class Meta:
        verbose_name = 'Ajouter Date de jour'
        verbose_name_plural = 'Ajouter Les Dates de jours'


class JourneeUtilisateur2021(models.Model):

    # LIST = [
    #     ('18', '18'),
    #     ('19', '19'),
    #     ('20', '20'),
    #     ('21', '21'),
    #     ('22', '22')
    # ]

    date = models.DateTimeField(auto_now_add=True)
    nom_de_societe = models.CharField(_("Nom de la société"), max_length=200)
    contact = models.CharField(_("Personne contact"), max_length=200)
    email = models.EmailField(_("Email"), max_length=250)
    accompagnee = models.CharField(
        _("Accompagnée de"), max_length=200, blank=True, null=True)
    # selected_date = models.CharField(_("Séléctionne une date"), max_length=5, choices=LIST, default="18")
    selected_date = models.ManyToManyField(SelectDate)

    def __str__(self):
        return self.nom_de_societe

    class Meta:
        verbose_name = 'Journée Utilisateurs 2021'
        verbose_name_plural = 'Journée Utilisateurs 2021'


class FormationArmaturesCube(models.Model):
    PRESENTATION = [
        ('sur place', 'Formation Armatures Cube Strakon sur place'),
        ('via internet', 'Formation Armatures Cube Strakon via Internet')
    ]
    BRANCH = [

        ('Ingénieur structurale', 'Ingénieur structurale'),
        ('Construction préfabriquée', 'Construction préfabriquée'),
        ('Architecture', 'Architecture'),
        ("Commerce de l'acier", "Commerce de l'acier"),
        ("Établissements d'enseignement", "Établissements d'enseignement"),
        ('Étudiant', 'Étudiant'),
        ('Autres', 'Autres')

    ]
    COUNTRIES = [
        ('Algérie', 'Algérie'),
        ('Afrique du Sud', 'Afrique du Sud'),
        ('Angola', 'Angola'),
        ('Bénin', 'Bénin'),
        ('Botswana', 'Botswana'),
        ('Burkina', 'Burkina'),
        ('Burundi', 'Burundi'),
        ('Cameroun', 'Cameroun'),
        ('Cap-Vert', 'Cap-Vert'),
        ('République centrafricaine', 'République centrafricaine'),
        ('Comores', 'Comores'),
        ('Congo', 'Congo'),
        ('République démocratique du Congo', 'République démocratique du Congo'),
        ("Côte d'Ivoire", "Côte d'Ivoire"),
        ('Djibouti', 'Djibouti'),
        ('Égypte', 'Égypte'),
        ('Érythrée', 'Érythrée'),
        ('Éthiopie', 'Éthiopie'),
        ('Gabon', 'Gabon'),
        ('Gambie', 'Gambie'),
        ('Ghana', 'Ghana'),
        ('Guinée', 'Guinée'),
        ('Guinée-Bissau', 'Guinée-Bissau'),
        ('Guinée équatoriale', 'Guinée équatoriale'),
        ('Kenya', 'Kenya'),
        ('Lesotho', 'Lesotho'),
        ('Libéria', 'Libéria'),
        ('Libye', 'Libye'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Mali', 'Mali'),
        ('Maroc', 'Maroc'),
        ('Maurice', 'Maurice'),
        ('Mauritanie', 'Mauritanie'),
        ('Mozambique', 'Mozambique'),
        ('Namibie', 'Namibie'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Ouganda', 'Ouganda'),
        ('Rwanda', 'Rwanda'),
        ('Sao Tomé-et-Principe', 'Sao Tomé-et-Principe'),
        ('Sénégal', 'Sénégal'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Somalie', 'Somalie'),
        ('Soudan', 'Soudan'),
        ('Sud-Soudan', 'Sud-Soudan'),
        ('Swaziland', 'Swaziland'),
        ('Tanzanie', 'Tanzanie'),
        ('Tchad', 'Tchad'),
        ('Togo', 'Togo'),
        ('Tunisie', 'Tunisie'),
        ('Zambie', 'Zambie'),
        ('Zimbabwe', 'Zimbabwe'),
        ('Antigua-et-Barbuda', 'Antigua-et-Barbuda'),
        ('Argentine', 'Argentine'),
        ('Bahamas', 'Bahamas'),
        ('Barbade', 'Barbade'),
        ('Belize', 'Belize'),
        ('Bolivie', 'Bolivie'),
        ('Brésil', 'Brésil'),
        ('Canada', 'Canada'),
        ('Chili', 'Chili'),
        ('Colombie', 'Colombie'),
        ('Costa Rica', 'Costa Rica'),
        ('Cuba', 'Cuba'),
        ('République dominicaine', 'République dominicaine'),
        ('Dominique', 'Dominique'),
        ('Équateur', 'Équateur'),
        ('États-Unis', 'États-Unis'),
        ('Grenade', 'Grenade'),
        ('Guatemala', 'Guatemala'),
        ('Guyana', 'Guyana'),
        ('Haïti', 'Haïti'),
        ('Honduras', 'Honduras'),
        ('Jamaïque', 'Jamaïque'),
        ('Mexique', 'Mexique'),
        ('Nicaragua', 'Nicaragua'),
        ('Panama', 'Panama'),
        ('Paraguay', 'Paraguay'),
        ('Pérou', 'Pérou'),
        ('Porto Rico', 'Porto Rico'),
        ('Saint-Christophe-et-Niévès', 'Saint-Christophe-et-Niévès'),
        ('Sainte-Lucie', 'Sainte-Lucie'),
        ('Saint-Vincent-et-les Grenadines', 'Saint-Vincent-et-les Grenadines'),
        ('Salvador', 'Salvador'),
        ('Suriname', 'Suriname'),
        ('Trinité-et-Tobago', 'Trinité-et-Tobago'),
        ('Uruguay', 'Uruguay'),
        ('Venezuela', 'Venezuela'),
        ('Afghanistan', 'Afghanistan'),
        ('Arabie saoudite', 'Arabie saoudite'),
        ('Bahreïn', 'Bahreïn'),
        ('Bangladesh', 'Bangladesh'),
        ('Bhoutan', 'Bhoutan'),
        ('Birmanie', 'Birmanie'),
        ('Brunei', 'Brunei'),
        ('Cambodge', 'Cambodge'),
        ('Chine', 'Chine'),
        ('Corée du Nord', 'Corée du Nord'),
        ('Corée du Sud', 'Corée du Sud'),
        ('Émirats arabes unis', 'Émirats arabes unis'),
        ('Inde', 'Inde'),
        ('Indonésie', 'Indonésie'),
        ('Irak', 'Irak'),
        ('Iran', 'Iran'),
        ('Palestine', 'Palestine'),
        ('Japon', 'Japon'),
        ('Jordanie', 'Jordanie'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kirghizistan', 'Kirghizistan'),
        ('Koweït', 'Koweït'),
        ('Laos', 'Laos'),
        ('Liban', 'Liban'),
        ('Malaisie', 'Malaisie'),
        ('Maldives', 'Maldives'),
        ('Mongolie', 'Mongolie'),
        ('Népal', 'Népal'),
        ('Oman', 'Oman'),
        ('Ouzbékistan', 'Ouzbékistan'),
        ('Pakistan', 'Pakistan'),
        ('Philippines', 'Philippines'),
        ('Qatar', 'Qatar'),
        ('Singapour', 'Singapour'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Syrie', 'Syrie'),
        ('Tadjikistan', 'Tadjikistan'),
        ('Taïwan', 'Taïwan'),
        ('Thaïlande', 'Thaïlande'),
        ('Timor oriental', 'Timor oriental'),
        ('Turkménistan', 'Turkménistan'),
        ('Turquie', 'Turquie'),
        ('Viêt Nam', 'Viêt Nam'),
        ('Yémen', 'Yémen'),
        ('Allemagne', 'Allemagne'),
        ('Albanie', 'Albanie'),
        ('Andorre', 'Andorre'),
        ('Arménie', 'Arménie'),
        ('Autriche', 'Autriche'),
        ('Azerbaïdjan', 'Azerbaïdjan'),
        ('Belgique', 'Belgique'),
        ('Biélorussie', 'Biélorussie'),
        ('Bosnie-Herzégovine', 'Bosnie-Herzégovine'),
        ('Bulgarie', 'Bulgarie'),
        ('Chypre', 'Chypre'),
        ('Croatie', 'Croatie'),
        ('Danemark', 'Danemark'),
        ('Espagne', 'Espagne'),
        ('Estonie', 'Estonie'),
        ('Finlande', 'Finlande'),
        ('France', 'France'),
        ('Géorgie', 'Géorgie'),
        ('Grèce', 'Grèce'),
        ('Hongrie', 'Hongrie'),
        ('Irlande', 'Irlande'),
        ('Islande', 'Islande'),
        ('Italie', 'Italie'),
        ('Lettonie', 'Lettonie'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lituanie', 'Lituanie'),
        ('Luxembourg', 'Luxembourg'),
        ('République de Macédoine', 'République de Macédoine'),
        ('Malte', 'Malte'),
        ('Moldavie', 'Moldavie'),
        ('Monaco', 'Monaco'),
        ('Monténégro', 'Monténégro'),
        ('Norvège', 'Norvège'),
        ('Pays-Bas', 'Pays-Bas'),
        ('Pologne', 'Pologne'),
        ('Portugal', 'Portugal'),
        ('République tchèque', 'République tchèque'),
        ('Roumanie', 'Roumanie'),
        ('Royaume-Uni', 'Royaume-Uni'),
        ('Russie', 'Russie'),
        ('Saint-Marin', 'Saint-Marin'),
        ('Serbie', 'Serbie'),
        ('Slovaquie', 'Slovaquie'),
        ('Slovénie', 'Slovénie'),
        ('Suède', 'Suède'),
        ('Suisse', 'Suisse'),
        ('Ukraine', 'Ukraine'),
        ('Vatican', 'Vatican'),
        ('Australie', 'Australie'),
        ('Fidji', 'Fidji'),
        ('Kiribati', 'Kiribati'),
        ('Marshall', 'Marshall'),
        ('Micronésie', 'Micronésie'),
        ('Nauru', 'Nauru'),
        ('Nouvelle-Zélande', 'Nouvelle-Zélande'),
        ('Palaos', 'Palaos'),
        ('Papouasie-Nouvelle-Guinée', 'Papouasie-Nouvelle-Guinée'),
        ('Salomon', 'Salomon'),
        ('Samoa', 'Samoa'),
        ('Tonga', 'Tonga'),
        ('Tuvalu', 'Tuvalu'),
        ('Vanuatu', 'Vanuatu'),
    ]
    post_date = models.DateTimeField(_("Publié"), auto_now_add=True)
    slug = slug = AutoSlugField(
        populate_from='societe', unique_with='societe', unique=True)
    type_presentation = models.CharField(
        _("Type de formation"), choices=PRESENTATION, max_length=50, default='via internet')

    branche = models.CharField(_("Branche"), choices=BRANCH, max_length=50)
    societe = models.CharField(_("Société"), max_length=50)
    contact = models.CharField(_("Contact"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    tel = models.CharField(_("Téléphone"), max_length=50)
    address = models.CharField(_("Adresse"), max_length=50)
    code_postal = models.CharField(_("Code Postal"), max_length=50)
    pays = models.CharField(_("Pays"), choices=COUNTRIES, max_length=50)

    class Meta:
        verbose_name = _("Formation Armatures Cube")
        verbose_name_plural = _("Formation Armatures Cube")

    def __str__(self):
        return self.societe

    def get_absolute_url(self):
        return reverse("fromation_detail", kwargs={"pk": self.pk})


class JourneeUtilisateur2022(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    nom_de_societe = models.CharField(_("Nom de la société"), max_length=200)
    contact = models.CharField(_("Personne contact"), max_length=200)
    email = models.EmailField(_("Email"), max_length=250)
    accompagnee = models.CharField(
        _("Accompagnée de"), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nom_de_societe

    class Meta:
        verbose_name = 'Journée Utilisateurs 2022'
        verbose_name_plural = 'Journée Utilisateurs 2022'

class JourneeUtilisateur2022plus(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    nom_de_societe = models.CharField(_("Nom de la société"), max_length=200)
    contact = models.CharField(_("Personne contact"), max_length=200)
    email = models.EmailField(_("Email"), max_length=250)
    accompagnee = models.CharField(
        _("Numéro de téléphone"), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nom_de_societe

    class Meta:
        verbose_name = 'Journée Utilisateurs 2022+'
        verbose_name_plural = 'Journée Utilisateurs 2022+'


class PresentationFromYoutube(models.Model):
    PRESENTATION = [
        ('sur place', 'Présentation du logiciel de CAO STRAKON sur place'),
        ('via internet', 'Présentation du logiciel de CAO STRAKON via Internet')
    ]
    BRANCH = [

        ('Ingénieur structurale', 'Ingénieur structurale'),
        ('Construction préfabriquée', 'Construction préfabriquée'),
        ('Architecture', 'Architecture'),
        ("Commerce de l'acier", "Commerce de l'acier"),
        ("Établissements d'enseignement", "Établissements d'enseignement"),
        ('Étudiant', 'Étudiant'),
        ('Autres', 'Autres')

    ]
    COUNTRIES = [
        ('Algérie', 'Algérie'),
        ('Afrique du Sud', 'Afrique du Sud'),
        ('Angola', 'Angola'),
        ('Bénin', 'Bénin'),
        ('Botswana', 'Botswana'),
        ('Burkina', 'Burkina'),
        ('Burundi', 'Burundi'),
        ('Cameroun', 'Cameroun'),
        ('Cap-Vert', 'Cap-Vert'),
        ('République centrafricaine', 'République centrafricaine'),
        ('Comores', 'Comores'),
        ('Congo', 'Congo'),
        ('République démocratique du Congo', 'République démocratique du Congo'),
        ("Côte d'Ivoire", "Côte d'Ivoire"),
        ('Djibouti', 'Djibouti'),
        ('Égypte', 'Égypte'),
        ('Érythrée', 'Érythrée'),
        ('Éthiopie', 'Éthiopie'),
        ('Gabon', 'Gabon'),
        ('Gambie', 'Gambie'),
        ('Ghana', 'Ghana'),
        ('Guinée', 'Guinée'),
        ('Guinée-Bissau', 'Guinée-Bissau'),
        ('Guinée équatoriale', 'Guinée équatoriale'),
        ('Kenya', 'Kenya'),
        ('Lesotho', 'Lesotho'),
        ('Libéria', 'Libéria'),
        ('Libye', 'Libye'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Mali', 'Mali'),
        ('Maroc', 'Maroc'),
        ('Maurice', 'Maurice'),
        ('Mauritanie', 'Mauritanie'),
        ('Mozambique', 'Mozambique'),
        ('Namibie', 'Namibie'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Ouganda', 'Ouganda'),
        ('Rwanda', 'Rwanda'),
        ('Sao Tomé-et-Principe', 'Sao Tomé-et-Principe'),
        ('Sénégal', 'Sénégal'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Somalie', 'Somalie'),
        ('Soudan', 'Soudan'),
        ('Sud-Soudan', 'Sud-Soudan'),
        ('Swaziland', 'Swaziland'),
        ('Tanzanie', 'Tanzanie'),
        ('Tchad', 'Tchad'),
        ('Togo', 'Togo'),
        ('Tunisie', 'Tunisie'),
        ('Zambie', 'Zambie'),
        ('Zimbabwe', 'Zimbabwe'),
        ('Antigua-et-Barbuda', 'Antigua-et-Barbuda'),
        ('Argentine', 'Argentine'),
        ('Bahamas', 'Bahamas'),
        ('Barbade', 'Barbade'),
        ('Belize', 'Belize'),
        ('Bolivie', 'Bolivie'),
        ('Brésil', 'Brésil'),
        ('Canada', 'Canada'),
        ('Chili', 'Chili'),
        ('Colombie', 'Colombie'),
        ('Costa Rica', 'Costa Rica'),
        ('Cuba', 'Cuba'),
        ('République dominicaine', 'République dominicaine'),
        ('Dominique', 'Dominique'),
        ('Équateur', 'Équateur'),
        ('États-Unis', 'États-Unis'),
        ('Grenade', 'Grenade'),
        ('Guatemala', 'Guatemala'),
        ('Guyana', 'Guyana'),
        ('Haïti', 'Haïti'),
        ('Honduras', 'Honduras'),
        ('Jamaïque', 'Jamaïque'),
        ('Mexique', 'Mexique'),
        ('Nicaragua', 'Nicaragua'),
        ('Panama', 'Panama'),
        ('Paraguay', 'Paraguay'),
        ('Pérou', 'Pérou'),
        ('Porto Rico', 'Porto Rico'),
        ('Saint-Christophe-et-Niévès', 'Saint-Christophe-et-Niévès'),
        ('Sainte-Lucie', 'Sainte-Lucie'),
        ('Saint-Vincent-et-les Grenadines', 'Saint-Vincent-et-les Grenadines'),
        ('Salvador', 'Salvador'),
        ('Suriname', 'Suriname'),
        ('Trinité-et-Tobago', 'Trinité-et-Tobago'),
        ('Uruguay', 'Uruguay'),
        ('Venezuela', 'Venezuela'),
        ('Afghanistan', 'Afghanistan'),
        ('Arabie saoudite', 'Arabie saoudite'),
        ('Bahreïn', 'Bahreïn'),
        ('Bangladesh', 'Bangladesh'),
        ('Bhoutan', 'Bhoutan'),
        ('Birmanie', 'Birmanie'),
        ('Brunei', 'Brunei'),
        ('Cambodge', 'Cambodge'),
        ('Chine', 'Chine'),
        ('Corée du Nord', 'Corée du Nord'),
        ('Corée du Sud', 'Corée du Sud'),
        ('Émirats arabes unis', 'Émirats arabes unis'),
        ('Inde', 'Inde'),
        ('Indonésie', 'Indonésie'),
        ('Irak', 'Irak'),
        ('Iran', 'Iran'),
        ('Palestine', 'Palestine'),
        ('Japon', 'Japon'),
        ('Jordanie', 'Jordanie'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kirghizistan', 'Kirghizistan'),
        ('Koweït', 'Koweït'),
        ('Laos', 'Laos'),
        ('Liban', 'Liban'),
        ('Malaisie', 'Malaisie'),
        ('Maldives', 'Maldives'),
        ('Mongolie', 'Mongolie'),
        ('Népal', 'Népal'),
        ('Oman', 'Oman'),
        ('Ouzbékistan', 'Ouzbékistan'),
        ('Pakistan', 'Pakistan'),
        ('Philippines', 'Philippines'),
        ('Qatar', 'Qatar'),
        ('Singapour', 'Singapour'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Syrie', 'Syrie'),
        ('Tadjikistan', 'Tadjikistan'),
        ('Taïwan', 'Taïwan'),
        ('Thaïlande', 'Thaïlande'),
        ('Timor oriental', 'Timor oriental'),
        ('Turkménistan', 'Turkménistan'),
        ('Turquie', 'Turquie'),
        ('Viêt Nam', 'Viêt Nam'),
        ('Yémen', 'Yémen'),
        ('Allemagne', 'Allemagne'),
        ('Albanie', 'Albanie'),
        ('Andorre', 'Andorre'),
        ('Arménie', 'Arménie'),
        ('Autriche', 'Autriche'),
        ('Azerbaïdjan', 'Azerbaïdjan'),
        ('Belgique', 'Belgique'),
        ('Biélorussie', 'Biélorussie'),
        ('Bosnie-Herzégovine', 'Bosnie-Herzégovine'),
        ('Bulgarie', 'Bulgarie'),
        ('Chypre', 'Chypre'),
        ('Croatie', 'Croatie'),
        ('Danemark', 'Danemark'),
        ('Espagne', 'Espagne'),
        ('Estonie', 'Estonie'),
        ('Finlande', 'Finlande'),
        ('France', 'France'),
        ('Géorgie', 'Géorgie'),
        ('Grèce', 'Grèce'),
        ('Hongrie', 'Hongrie'),
        ('Irlande', 'Irlande'),
        ('Islande', 'Islande'),
        ('Italie', 'Italie'),
        ('Lettonie', 'Lettonie'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lituanie', 'Lituanie'),
        ('Luxembourg', 'Luxembourg'),
        ('République de Macédoine', 'République de Macédoine'),
        ('Malte', 'Malte'),
        ('Moldavie', 'Moldavie'),
        ('Monaco', 'Monaco'),
        ('Monténégro', 'Monténégro'),
        ('Norvège', 'Norvège'),
        ('Pays-Bas', 'Pays-Bas'),
        ('Pologne', 'Pologne'),
        ('Portugal', 'Portugal'),
        ('République tchèque', 'République tchèque'),
        ('Roumanie', 'Roumanie'),
        ('Royaume-Uni', 'Royaume-Uni'),
        ('Russie', 'Russie'),
        ('Saint-Marin', 'Saint-Marin'),
        ('Serbie', 'Serbie'),
        ('Slovaquie', 'Slovaquie'),
        ('Slovénie', 'Slovénie'),
        ('Suède', 'Suède'),
        ('Suisse', 'Suisse'),
        ('Ukraine', 'Ukraine'),
        ('Vatican', 'Vatican'),
        ('Australie', 'Australie'),
        ('Fidji', 'Fidji'),
        ('Kiribati', 'Kiribati'),
        ('Marshall', 'Marshall'),
        ('Micronésie', 'Micronésie'),
        ('Nauru', 'Nauru'),
        ('Nouvelle-Zélande', 'Nouvelle-Zélande'),
        ('Palaos', 'Palaos'),
        ('Papouasie-Nouvelle-Guinée', 'Papouasie-Nouvelle-Guinée'),
        ('Salomon', 'Salomon'),
        ('Samoa', 'Samoa'),
        ('Tonga', 'Tonga'),
        ('Tuvalu', 'Tuvalu'),
        ('Vanuatu', 'Vanuatu'),
    ]
    post_date = models.DateTimeField(_("Publié"), auto_now_add=True)
    slug = slug = AutoSlugField(
        populate_from='societe', unique_with='societe', unique=True)
    type_presentation = models.CharField(
        _("Type de présentation"), choices=PRESENTATION, max_length=50, default='via internet')

    branche = models.CharField(_("Branche"), choices=BRANCH, max_length=50)
    societe = models.CharField(_("Société"), max_length=50)
    contact = models.CharField(_("Contact"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    tel = models.CharField(_("Téléphone"), max_length=50)
    address = models.CharField(_("Adresse"), max_length=50)
    code_postal = models.CharField(_("Code Postal"), max_length=50)
    pays = models.CharField(_("Pays"), choices=COUNTRIES, max_length=50)

    class Meta:
        verbose_name = _("Presentation Youtuber")
        verbose_name_plural = _("Presentations Youtuber")

    def __str__(self):
        return self.societe

    def get_absolute_url(self):
        return reverse("presentation_detail", kwargs={"pk": self.pk})


class Batimat(models.Model):
    COUNTRIES = [
        ('Algérie', 'Algérie'),
        ('Afrique du Sud', 'Afrique du Sud'),
        ('Angola', 'Angola'),
        ('Bénin', 'Bénin'),
        ('Botswana', 'Botswana'),
        ('Burkina', 'Burkina'),
        ('Burundi', 'Burundi'),
        ('Cameroun', 'Cameroun'),
        ('Cap-Vert', 'Cap-Vert'),
        ('République centrafricaine', 'République centrafricaine'),
        ('Comores', 'Comores'),
        ('Congo', 'Congo'),
        ('République démocratique du Congo', 'République démocratique du Congo'),
        ("Côte d'Ivoire", "Côte d'Ivoire"),
        ('Djibouti', 'Djibouti'),
        ('Égypte', 'Égypte'),
        ('Érythrée', 'Érythrée'),
        ('Éthiopie', 'Éthiopie'),
        ('Gabon', 'Gabon'),
        ('Gambie', 'Gambie'),
        ('Ghana', 'Ghana'),
        ('Guinée', 'Guinée'),
        ('Guinée-Bissau', 'Guinée-Bissau'),
        ('Guinée équatoriale', 'Guinée équatoriale'),
        ('Kenya', 'Kenya'),
        ('Lesotho', 'Lesotho'),
        ('Libéria', 'Libéria'),
        ('Libye', 'Libye'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Mali', 'Mali'),
        ('Maroc', 'Maroc'),
        ('Maurice', 'Maurice'),
        ('Mauritanie', 'Mauritanie'),
        ('Mozambique', 'Mozambique'),
        ('Namibie', 'Namibie'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Ouganda', 'Ouganda'),
        ('Rwanda', 'Rwanda'),
        ('Sao Tomé-et-Principe', 'Sao Tomé-et-Principe'),
        ('Sénégal', 'Sénégal'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Somalie', 'Somalie'),
        ('Soudan', 'Soudan'),
        ('Sud-Soudan', 'Sud-Soudan'),
        ('Swaziland', 'Swaziland'),
        ('Tanzanie', 'Tanzanie'),
        ('Tchad', 'Tchad'),
        ('Togo', 'Togo'),
        ('Tunisie', 'Tunisie'),
        ('Zambie', 'Zambie'),
        ('Zimbabwe', 'Zimbabwe'),
        ('Antigua-et-Barbuda', 'Antigua-et-Barbuda'),
        ('Argentine', 'Argentine'),
        ('Bahamas', 'Bahamas'),
        ('Barbade', 'Barbade'),
        ('Belize', 'Belize'),
        ('Bolivie', 'Bolivie'),
        ('Brésil', 'Brésil'),
        ('Canada', 'Canada'),
        ('Chili', 'Chili'),
        ('Colombie', 'Colombie'),
        ('Costa Rica', 'Costa Rica'),
        ('Cuba', 'Cuba'),
        ('République dominicaine', 'République dominicaine'),
        ('Dominique', 'Dominique'),
        ('Équateur', 'Équateur'),
        ('États-Unis', 'États-Unis'),
        ('Grenade', 'Grenade'),
        ('Guatemala', 'Guatemala'),
        ('Guyana', 'Guyana'),
        ('Haïti', 'Haïti'),
        ('Honduras', 'Honduras'),
        ('Jamaïque', 'Jamaïque'),
        ('Mexique', 'Mexique'),
        ('Nicaragua', 'Nicaragua'),
        ('Panama', 'Panama'),
        ('Paraguay', 'Paraguay'),
        ('Pérou', 'Pérou'),
        ('Porto Rico', 'Porto Rico'),
        ('Saint-Christophe-et-Niévès', 'Saint-Christophe-et-Niévès'),
        ('Sainte-Lucie', 'Sainte-Lucie'),
        ('Saint-Vincent-et-les Grenadines', 'Saint-Vincent-et-les Grenadines'),
        ('Salvador', 'Salvador'),
        ('Suriname', 'Suriname'),
        ('Trinité-et-Tobago', 'Trinité-et-Tobago'),
        ('Uruguay', 'Uruguay'),
        ('Venezuela', 'Venezuela'),
        ('Afghanistan', 'Afghanistan'),
        ('Arabie saoudite', 'Arabie saoudite'),
        ('Bahreïn', 'Bahreïn'),
        ('Bangladesh', 'Bangladesh'),
        ('Bhoutan', 'Bhoutan'),
        ('Birmanie', 'Birmanie'),
        ('Brunei', 'Brunei'),
        ('Cambodge', 'Cambodge'),
        ('Chine', 'Chine'),
        ('Corée du Nord', 'Corée du Nord'),
        ('Corée du Sud', 'Corée du Sud'),
        ('Émirats arabes unis', 'Émirats arabes unis'),
        ('Inde', 'Inde'),
        ('Indonésie', 'Indonésie'),
        ('Irak', 'Irak'),
        ('Iran', 'Iran'),
        ('Palestine', 'Palestine'),
        ('Japon', 'Japon'),
        ('Jordanie', 'Jordanie'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kirghizistan', 'Kirghizistan'),
        ('Koweït', 'Koweït'),
        ('Laos', 'Laos'),
        ('Liban', 'Liban'),
        ('Malaisie', 'Malaisie'),
        ('Maldives', 'Maldives'),
        ('Mongolie', 'Mongolie'),
        ('Népal', 'Népal'),
        ('Oman', 'Oman'),
        ('Ouzbékistan', 'Ouzbékistan'),
        ('Pakistan', 'Pakistan'),
        ('Philippines', 'Philippines'),
        ('Qatar', 'Qatar'),
        ('Singapour', 'Singapour'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Syrie', 'Syrie'),
        ('Tadjikistan', 'Tadjikistan'),
        ('Taïwan', 'Taïwan'),
        ('Thaïlande', 'Thaïlande'),
        ('Timor oriental', 'Timor oriental'),
        ('Turkménistan', 'Turkménistan'),
        ('Turquie', 'Turquie'),
        ('Viêt Nam', 'Viêt Nam'),
        ('Yémen', 'Yémen'),
        ('Allemagne', 'Allemagne'),
        ('Albanie', 'Albanie'),
        ('Andorre', 'Andorre'),
        ('Arménie', 'Arménie'),
        ('Autriche', 'Autriche'),
        ('Azerbaïdjan', 'Azerbaïdjan'),
        ('Belgique', 'Belgique'),
        ('Biélorussie', 'Biélorussie'),
        ('Bosnie-Herzégovine', 'Bosnie-Herzégovine'),
        ('Bulgarie', 'Bulgarie'),
        ('Chypre', 'Chypre'),
        ('Croatie', 'Croatie'),
        ('Danemark', 'Danemark'),
        ('Espagne', 'Espagne'),
        ('Estonie', 'Estonie'),
        ('Finlande', 'Finlande'),
        ('France', 'France'),
        ('Géorgie', 'Géorgie'),
        ('Grèce', 'Grèce'),
        ('Hongrie', 'Hongrie'),
        ('Irlande', 'Irlande'),
        ('Islande', 'Islande'),
        ('Italie', 'Italie'),
        ('Lettonie', 'Lettonie'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lituanie', 'Lituanie'),
        ('Luxembourg', 'Luxembourg'),
        ('République de Macédoine', 'République de Macédoine'),
        ('Malte', 'Malte'),
        ('Moldavie', 'Moldavie'),
        ('Monaco', 'Monaco'),
        ('Monténégro', 'Monténégro'),
        ('Norvège', 'Norvège'),
        ('Pays-Bas', 'Pays-Bas'),
        ('Pologne', 'Pologne'),
        ('Portugal', 'Portugal'),
        ('République tchèque', 'République tchèque'),
        ('Roumanie', 'Roumanie'),
        ('Royaume-Uni', 'Royaume-Uni'),
        ('Russie', 'Russie'),
        ('Saint-Marin', 'Saint-Marin'),
        ('Serbie', 'Serbie'),
        ('Slovaquie', 'Slovaquie'),
        ('Slovénie', 'Slovénie'),
        ('Suède', 'Suède'),
        ('Suisse', 'Suisse'),
        ('Ukraine', 'Ukraine'),
        ('Vatican', 'Vatican'),
        ('Australie', 'Australie'),
        ('Fidji', 'Fidji'),
        ('Kiribati', 'Kiribati'),
        ('Marshall', 'Marshall'),
        ('Micronésie', 'Micronésie'),
        ('Nauru', 'Nauru'),
        ('Nouvelle-Zélande', 'Nouvelle-Zélande'),
        ('Palaos', 'Palaos'),
        ('Papouasie-Nouvelle-Guinée', 'Papouasie-Nouvelle-Guinée'),
        ('Salomon', 'Salomon'),
        ('Samoa', 'Samoa'),
        ('Tonga', 'Tonga'),
        ('Tuvalu', 'Tuvalu'),
        ('Vanuatu', 'Vanuatu'),
    ]

    FUNCTION = [
        ('1', 'Particulier'),
        ('2', 'Étudiant'),
        ('3', 'Salarié'),
    ]
    subscriber_type = models.CharField(_("S'inscrire en tant que"),choices=FUNCTION, max_length=10)
    nom_ou_societe = models.CharField(_('Société ou école'), max_length=200, blank=True, null=True)
    contact = models.CharField(_('Contact'), max_length=200)
    email = models.EmailField(_('Email'), max_length=200)
    phone = models.CharField(_('Téléphone'), max_length=200)
    address = models.CharField(_('Adresse'), max_length=200)
    code = models.CharField(_('Code Postal'), max_length=200)
    # country = models.CharField(_('Pays'), choices=COUNTRIES ,max_length=200)
    pays = models.ForeignKey(Country, on_delete=models.CASCADE)
    ville = ChainedForeignKey(City, chained_field="pays", chained_model_field="country", auto_choose=True,sort=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_ou_societe
