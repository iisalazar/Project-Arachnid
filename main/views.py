from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView
from staff.models import Announcement, News, Organization, ResearchPaper
from django.utils import timezone
# Create your views here.

class IndexView(TemplateView):
    template_name = 'main/index.html'

class AdmissionView(TemplateView):
    template_name = 'main/admissions.html'

class NewsView(ListView):
    template_name = 'main/news.html'
    model = News
    context_object_name = "news"
    def get_queryset(self):
        return News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class NewsDetailView(DetailView):
    template_name = "main/news_details.html"
    model = News
    context_object_name = "news"
    pk_url_kwarg = 'pk'

class OrganizationView(TemplateView):
    template_name = 'main/orgs.html'

class AppliedListView(ListView):
    template_name = 'main/appliedScience.html'
    model = ResearchPaper
    context_object_name = "research_paper"
    def get_queryset(self):
        return ResearchPaper.objects.filter(category="Applied").order_by('-published_date')

class AppliedDetailView(DetailView):
    template_name = 'main/appliedScience_detail.html'
    model = ResearchPaper
    context_object_name = "applied_science_research"
    pk_url_kwarg = "pk"

class LifeListView(ListView):
    template_name = 'main/lifeScience.html'
    model = ResearchPaper
    context_object_name = "research_paper"
    def get_queryset(self):
        return ResearchPaper.objects.filter(category="Life").order_by('-published_date')

class LifeDetailView(DetailView):
    template_name = 'main/lifeScience_detail.html'
    model = ResearchPaper
    context_object_name = "life_science_research"
    pk_url_kwarg = "pk"

class AboutView(TemplateView):
    template_name = 'main/about.html'

class FAQsView(TemplateView):
    template_name = 'main/faqs.html'


#############################
# THIS IS FOR THE STAFF APP #
#############################

class StaffIndexView(TemplateView):
    template_name = 'staff/index.html'

class AnnouncementView(ListView):
    template_name = 'staff/announcements.html'
