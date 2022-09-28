from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail, EmailMultiAlternatives
from django.views.generic.base import TemplateView
from video.models import FormationVideo
from .models import (
    Blog,
    Gallery,
    PresentationFromYoutube,
    Video,
    Presentation,
    LicenceEtudiant,
    LicenceEtablissement,
    BlogCategories,
    JourneeUtilisateur2021,
    SelectDate,
    FormationArmaturesCube,
    JourneeUtilisateur2022,
    JourneeUtilisateur2022plus,
    Batimat
)
from .forms import (
    BlogForm,
    BlogCategoriesForm,
    GalleryForm,
    PresentationYoutuberForm,
    VideoForm,
    PresentationForm,
    LicenceEtudiantForm,
    LicenceEtablissementForm,
    JourneeUtilisateur2021Form,
    JourneeUtilisateur2022Form,
    JourneeUtilisateur2022PlusForm,
    FormationArmaturesCubeForm,
    BatimatForm
)


def accueil(request):
    blog_list = Blog.objects.all().order_by('-post_date')[:5]
    blog_list_img = Blog.objects.all().order_by('-post_date')[:1]
    video_list = Video.objects.all().order_by('-post_date')[:5]
    video_list_title = Video.objects.all().order_by('-post_date')[:4]
    latest_video = Video.objects.all().order_by('-post_date')[:1]
    context = {
        'blog_list': blog_list,
        'blog_list_img': blog_list_img,
        'video_list': video_list,
        'video_list_title': video_list_title,
        'latest_video': latest_video
    }
    return render(request, 'views/accueil.html', context)

# logiciel et solution


def logiciel_cao(request):
    return render(request, 'views/logiciel_et_solution/logiciel_cao.html')


def ing_de_construction(request):
    blog_list = Blog.objects.all().order_by('-post_date')[:5]
    return render(request, 'views/logiciel_et_solution/ing_de_construction.html', {'blog_list': blog_list})


def construction_de_batiment(request):
    blog_list = Blog.objects.all().order_by('-post_date')[:5]
    return render(request, 'views/logiciel_et_solution/construction_de_batiment.html', {'blog_list': blog_list})


def pieces_pref_structurelles(request):
    blog_list = Blog.objects.all().order_by('-post_date')[:5]
    return render(request, 'views/logiciel_et_solution/pieces_pref_structurelles.html', {'blog_list': blog_list})


def pieces_pref_unitisees(request):
    blog_list = Blog.objects.all().order_by('-post_date')[:5]
    return render(request, 'views/logiciel_et_solution/pieces_pref_unitisees.html', {'blog_list': blog_list})


def bim(request):
    blog_list = Blog.objects.all().order_by('-post_date')[:5]
    return render(request, 'views/logiciel_et_solution/bim.html', {'blog_list': blog_list})


def architecture_ing_en_structure(request):
    blog_list = Blog.objects.all().order_by('-post_date')[:5]
    return render(request, 'views/logiciel_et_solution/architecture_ing_en_structure.html', {'blog_list': blog_list})


def interfaces(request):
    blog_list = Blog.objects.all().order_by('-post_date')[:5]
    return render(request, 'views/logiciel_et_solution/interfaces.html', {'blog_list': blog_list})

# Services


def service_et_assistance(request):
    return render(request, 'views/services/service_et_assistance.html')


def demande_presentation(request):
    return render(request, 'views/services/demande_presentation.html')


def telechargement(request):
    return render(request, 'views/services/telechargement.html')

# --------extra info for download--------------------


def patch4(request):
    return render(request, 'views/services/extra/2020/patch/patch4.html')

# --------End extra info for download ---------------


def faq(request):
    return render(request, 'views/services/faq.html')

# pages


def contact(request):
    return render(request, 'views/contact.html')


def licence(request):
    return render(request, 'views/licence.html')


class GalerieView(ListView):
    model = Gallery
    template_name = 'views/galerie.html'
    ordering = ['-post_date']
    paginate_by = 12


class VideoView(ListView):
    model = Video
    template_name = 'views/videos.html'
    ordering = ['-post_date']
    paginate_by = 9


class PresentationView(SuccessMessageMixin, CreateView):
    model = Presentation
    template_name = 'views/services/demande_presentation.html'
    form_class = PresentationForm
    success_url = reverse_lazy('demande_presentation')
    success_message = "Merci, vos demandes sont envoyées, un commercial vous contactera dans les plus brefs délais."

    def form_valid(self, form):
        subject = "Notification demande de présentation"
        msg = "Nous avons reçu une nouvelle demande de présentation \nvous pouvez la verfier sur www.strakon.fr/myadmin"
        send_mail(subject, msg, 'noreply@strakon.fr',
                  ["contact@wibim.fr"], fail_silently=False, )
        return super().form_valid(form)


class LicenceEtudiantView(SuccessMessageMixin, CreateView):
    model = LicenceEtudiant
    template_name = 'views/services/licences/etudiant.html'
    form_class = LicenceEtudiantForm
    success_url = reverse_lazy('etudiant')
    success_message = "Merci, vos demandes sont envoyées, un commercial vous contactera dans les plus brefs délais."

    def form_valid(self, form):
        subject = "Notification demande de Licence étudiant"
        msg = "Nous avons reçu une nouvelle demande de licence étudiant \nvous pouvez la verfier sur www.strakon.fr/myadmin"
        send_mail(subject, msg, 'noreply@strakon.fr',
                  ["contact@wibim.fr"], fail_silently=False, )
        return super().form_valid(form)


class LicenceEtablissementView(SuccessMessageMixin, CreateView):
    model = LicenceEtablissement
    template_name = 'views/services/licences/educative.html'
    form_class = LicenceEtablissementForm
    success_url = reverse_lazy('educative')
    success_message = "Merci, vos demandes sont envoyées, un commercial vous contactera dans les plus brefs délais."

    def form_valid(self, form):
        subject = "Notification demande de Licence éducative"
        msg = "Nous avons reçu une nouvelle demande de licence éducative pour un établissment d'enseignement \nvous pouvez la verfier sur www.strakon.fr/myadmin"
        send_mail(subject, msg, 'noreply@strakon.fr',
                  ["contact@wibim.fr"], fail_silently=False, )
        return super().form_valid(form)


class BlogView(ListView):
    model = Blog
    template_name = 'views/actualites.html'
    context_object_name = 'blog_list'
    ordering = ['-post_date']
    paginate_by = 5


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'views/actualites_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["blog_list"] = Blog.objects.all().order_by('-post_date')[:5]
        return context


def cookies_policy(request):
    return render(request, 'rules/cookies_policy.html')


def privacy_policy(request):
    return render(request, 'rules/privacy_policy.html')


def terms_and_conditions(request):
    return render(request, 'rules/terms_and_conditions.html')


# Admin Gestionnaire
@login_required
def dashboard(request):
    news = Blog.objects.all().order_by('-post_date')[:3]
    licence_etudiant = LicenceEtudiant.objects.all().order_by('-post_date')[:5]
    licence_educative = LicenceEtablissement.objects.all().order_by(
        '-post_date')[:5]
    presentation = Presentation.objects.all().order_by('-post_date')[:5]
    video = Video.objects.all().order_by('-post_date')[:5]
    galerie = Gallery.objects.all().order_by('-post_date')[:5]

    context = {
        'news': news,
        'licence_etudiant': licence_etudiant,
        'licence_educative': licence_educative,
        'presentation': presentation,
        'video': video,
        'galerie': galerie
    }
    return render(request, 'views/admin/index.html', context)


class AddArticleView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_required = True
    model = Blog
    template_name = "views/admin/posts/ajouter-articles.html"
    form_class = BlogForm
    success_url = reverse_lazy('ajouter-article')
    success_message = "Article ajouter avec success."

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListeArticleView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Blog
    template_name = "views/admin/posts/listes-articles.html"
    ordering = ['-post_date']
    paginate_by = 10


class EditArticleView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    template_name = "views/admin/posts/modifier-articles.html"
    form_class = BlogForm
    success_url = reverse_lazy('listes-articles')
    success_message = 'Votre article a été mis à jour avec succès'


class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "views/admin/posts/supprimer-articles.html"
    success_url = reverse_lazy('listes-articles')
    success_message = 'Un article a été supprimer'

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteArticleView, self).delete(request, *args, **kwargs)


class BlogCategoriesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = BlogCategories
    template_name = "views/admin/posts/categories.html"
    form_class = BlogCategoriesForm
    success_url = reverse_lazy('categorie')
    success_message = 'Catégorie enregistrer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = BlogCategories.objects.all().order_by('-post_date')
        return context


class BlogCategoriesDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogCategories
    template_name = "views/admin/posts/supprimer-categories.html"
    success_url = reverse_lazy('categorie')
    success_message = 'Une catégorie a été supprimer'

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(BlogCategoriesDeleteView, self).delete(request, *args, **kwargs)


class BlogCategoriesUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogCategories
    template_name = "views/admin/posts/modifier-categories.html"
    form_class = BlogCategoriesForm
    success_url = reverse_lazy('categorie')
    success_message = 'Votre catégorie a été mis à jour avec succès'


class PresentationListView(LoginRequiredMixin, ListView):
    model = Presentation
    template_name = "views/admin/presentation.html"
    ordering = ['-post_date']
    paginate_by = 10


class LicenceEtudiantListView(LoginRequiredMixin, ListView):
    model = LicenceEtudiant
    template_name = "views/admin/licence-etudiant.html"
    ordering = ['-post_date']
    paginate_by = 10
    # success_url = reverse_lazy('etudiant-list')

    # def form_valid(self, form):
    #     subject, from_email, to = "Licence d'étudiant Strakon", 'noreply@strakon.fr', 'webmaster@gisysco.com'
    #     text_content = "Nous vous remercions de l’intérêt que vous apporté à notre logiciel STRAKON"
    #     html_content = "<p>Afin de le pratiqué, veuillez le télécharger <br><a href='https://download.strakon.fr/2020/complet/patch4/STRAKON2020.zip'>STRAKON 2020</a></p>"
    #     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send(fail_silently=False)
    #     return super().form_valid(form)


class LicenceEtablissementListView(LoginRequiredMixin, ListView):
    model = LicenceEtablissement
    template_name = "views/admin/licence-educative.html"
    ordering = ['-post_date']
    paginate_by = 10


class VideoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Video
    template_name = "views/admin/videos/ajouter.html"
    form_class = VideoForm
    success_url = reverse_lazy('list-video')
    success_message = 'Vidéo enregistrer'


class VideoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Video
    template_name = "views/admin/videos/modifier.html"
    form_class = VideoForm
    success_url = reverse_lazy('list-video')
    success_message = 'Votre vidéo a été mis à jour avec succès'


class VideoDeleteView(LoginRequiredMixin, DeleteView):
    model = Video
    template_name = "views/admin/videos/supprimer.html"
    success_url = reverse_lazy('list-video')
    success_message = 'Vidéo supprimer'

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(VideoDeleteView, self).delete(request, *args, **kwargs)


class VideoListView(LoginRequiredMixin, ListView):
    model = Video
    template_name = "views/admin/videos/list.html"
    ordering = ['-post_date']
    paginate_by = 10


class GalleryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Gallery
    template_name = "views/admin/galeries/ajouter.html"
    form_class = GalleryForm
    success_url = reverse_lazy('gallery-list')
    success_message = 'Image enregistrer'


class GalleryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Gallery
    template_name = "views/admin/galeries/modifier.html"
    form_class = GalleryForm
    success_url = reverse_lazy('gallery-list')
    success_message = 'Votre image a été mis à jour avec succès'


class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    model = Gallery
    template_name = "views/admin/galeries/supprimer.html"
    success_url = reverse_lazy('gallery-list')
    success_message = 'Image supprimer'

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(GalleryDeleteView, self).delete(request, *args, **kwargs)


class GalleryListView(LoginRequiredMixin, ListView):
    model = Gallery
    template_name = "views/admin/galeries/list.html"
    ordering = ['-post_date']
    paginate_by = 10


def condition_licence_etudiant(request):
    return render(request, 'views/services/licences/condition_etudiant.html')


def condition_licence_educative(request):
    return render(request, 'views/services/licences/condition_educative.htm')


class JourneeUtilisateur2021CreateView(SuccessMessageMixin, CreateView):
    model = JourneeUtilisateur2021
    template_name = "docs/2021/form.html"
    form_class = JourneeUtilisateur2021Form
    success_url = reverse_lazy('j2021')
    success_message = 'Votre inscription est enregistrer avec succées'

    def form_valid(self, form):
        subject = "Nouveaux inscription au journée utilisateur 2021"
        msg = "Nous avons reçu une nouvelle inscription au journée utilisateur 2021\nvous pouvez la verfier sur www.strakon.fr/myadmin"
        send_mail(subject, msg, 'noreply@strakon.fr',
                  ["webmaster@gisysco.com"], fail_silently=False, )
        return super().form_valid(form)


@login_required
def list_subscriber_2021(request):
    selected_date = SelectDate.objects.all()
    subscriber = JourneeUtilisateur2021.objects.all()

    context = {
        'selected_date': selected_date,
        'subscriber': subscriber
    }
    return render(request, 'views/admin/journy-list.html', context)


class FormationArmaturesCubeCreateView(SuccessMessageMixin, CreateView):
    model = FormationArmaturesCube
    template_name = 'views/services/formation_armatures_cube.html'
    form_class = FormationArmaturesCubeForm
    success_url = reverse_lazy('formation')
    success_message = "Merci, votre demande est envoyée, un commercial vous contactera dans les plus brefs délais."

    def form_valid(self, form):
        subject = "Nouveau demande de formation Strakon Armatures Cube"
        msg = "Nous avons reçu une nouvelle demande de formation de Strakon 2021 Armatures Cube\nvous pouvez la verfier sur www.strakon.fr/myadmin/formation/list/"
        send_mail(subject, msg, 'noreply@strakon.fr',
                  ["contact@wibim.fr"], fail_silently=False)
        return super().form_valid(form)


class FormationArmaturesCubeListView(LoginRequiredMixin, ListView):
    model = FormationArmaturesCube
    template_name = "views/admin/fromation.html"
    ordering = ['-post_date']
    paginate_by = 10


class JU2022CreateView(SuccessMessageMixin, CreateView):
    model = JourneeUtilisateur2022
    template_name = "docs/2022/form.html"
    form_class = JourneeUtilisateur2022Form
    success_url = reverse_lazy('journe22')
    success_message = 'Votre inscription est enregistrer avec succées'

    def form_valid(self, form):
        subject = "Nouveaux inscription au journée utilisateur 2022"
        msg = "Nous avons reçu une nouvelle inscription au journée utilisateur 2022\nvous pouvez la verfier sur www.strakon.fr/myadmin"
        send_mail(subject, msg, 'noreply@strakon.fr',
                  ["webmaster@gisysco.com"], fail_silently=False, )
        return super().form_valid(form)


@login_required
def list_subscriber_2022(request):
    # selected_date = SelectDate.objects.all()
    subscriber = JourneeUtilisateur2022.objects.all()

    context = {
        # 'selected_date': selected_date,
        'subscriber': subscriber
    }
    return render(request, 'views/admin/journy-list22.html', context)


class JU2022PlusCreateView(SuccessMessageMixin, CreateView):
    model = JourneeUtilisateur2022plus
    template_name = "docs/2022/form2.html"
    form_class = JourneeUtilisateur2022PlusForm
    success_url = reverse_lazy('journe22plus')
    success_message = 'Votre inscription est enregistrer avec succées'

    def form_valid(self, form):
        subject = "Initiation Armatures Cube Strakon 2022+"
        msg = "Nous avons reçu une nouvelle inscription au journée utilisateur 2022\nvous pouvez la verfier sur www.strakon.fr/myadmin/list-journee-utilisateur-2022-plus/"
        send_mail(subject, msg, 'noreply@strakon.fr',
                  ["it-admin@gisysco.com"], fail_silently=False, )
        return super().form_valid(form)


class JU2022PlusListView(LoginRequiredMixin, ListView):
    model = JourneeUtilisateur2022plus
    template_name = 'views/admin/journy-list22plus.html'


class PresentationViewYoutuber(SuccessMessageMixin, CreateView):
    model = PresentationFromYoutube
    template_name = 'views/services/spec/presentation_youtube.html'
    form_class = PresentationYoutuberForm
    success_url = reverse_lazy('demande_yt')
    success_message = "Merci, vos demandes sont envoyées, un commercial vous contactera dans les plus brefs délais."

    def form_valid(self, form):
        subject = "Notification demande de présentation redirigé de Youtube"
        msg = "Nous avons reçu une nouvelle demande de présentation redirigé de la chaine Youtube VINCENT CAVUOTO \nvous pouvez la verfier sur www.strakon.fr/myadmin/demander/presentaion/analyse-youtube/"
        send_mail(subject, msg, 'noreply@strakon.fr',
                  ["contact@wibim.fr"], fail_silently=False, )
        return super().form_valid(form)


class PresentationFromyoutubeListView(LoginRequiredMixin, ListView):
    model = PresentationFromYoutube
    template_name = "views/admin/presentation_youtube_list.html"
    ordering = ['-post_date']
    paginate_by = 10


class TrainingView(ListView):
    model = FormationVideo
    template_name = "views/training.html"


class BatimatView(SuccessMessageMixin, CreateView):

    model = Batimat
    form_class = BatimatForm
    template_name = 'event/subscribe.html'
    success_url = reverse_lazy('batimat-event')
    success_message = 'Votre inscription est enregistrer avec succées'


class BatimatListView(LoginRequiredMixin, ListView):
    model = Batimat
    template_name = 'event/list.html'
    ordering = ['-date']
    paginate_by = 10
