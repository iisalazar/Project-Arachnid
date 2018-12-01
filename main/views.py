from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView
from staff.models import Announcement, News, Organization, ResearchPaper
from django.utils import timezone
# Create your views here.


# Returns a list of announcements and news
# Does not check if the query result is none
def index(request):
    announcements = list(Announcement.objects.order_by('-date_created')[:5])
    news = list(News.objects.order_by('-published_date')[:5])
    #announcements = get_list_or_404(Announcement.objects.order_by('-date_created')[:5])
    #news = get_list_or_404(News.objects.order_by('-published_date')[:5])
    return render(request, 'main/index.html', {'announcements': announcements, 'news': news})


class AnnouncementDetailView(DetailView):
    model = Announcement
    context_object_name = "announcement"
    pk_url_kwarg = 'pk'

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

class OrganizationListView(ListView):
    template_name = 'main/orgs.html'
    model = Organization
    context_object_name = "organizations"
    def get_queryset(self):
        return Organization.objects.all()

class OrganizationDetailView(DetailView):
    template_name = 'main/orgs_detail.html'
    model = Organization
    context_object_name = "organization"
    pk_url_kwarg = "pk"
    



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
