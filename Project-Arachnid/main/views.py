from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView, RedirectView
from django.core.paginator import Paginator

from announcements.forms import AnnouncementForm
from news.forms import NewsForm
from organizations.forms import OrganizationForm, OrganizationHRForm
from research.forms import ResearchForm, ResearchProponentForm


from announcements.models import Announcement
from news.models import News
from organizations.models import Organization, OrganizationOfficer
from research.models import ResearchPaper, ResearchProponent

from django.utils import timezone
# Create your views here.


# Returns a list of announcements and news
# Does not check if the query result is none
def index(request):
    announcements = list(Announcement.objects.order_by('-date_created')[:5])
    news = list(News.objects.order_by('-published_date')[:5])
    if len(announcements) > 0:
        announcement_latest = announcements.pop(0)
    else:
        announcement_latest = None
    if len(news) > 0:
        news_latest = news.pop(0) or None
    else:
        news_latest = None
    #announcements = get_list_or_404(Announcement.objects.order_by('-date_created')[:5])
    #news = get_list_or_404(News.objects.order_by('-published_date')[:5])
    data = {
            'announcements': announcements, 
            'news': news,
            'latest_announcement' : announcement_latest,
            'latest_news' : news_latest
            }
    return render(request, 'main/index.html', data)

class AnnouncementRedirectView(RedirectView):
    pattern_name = 'main:announcement_list'
    permanent = True
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        kwargs['page'] = 1
        return super().get_redirect_url(*args, **kwargs)


class AnnouncementListView(ListView):
    template_name = 'main/announcement_list.html'
    model = Announcement
    context_object_name = "announcements"
    paginated_by = 10

    def get_queryset(self, *args, **kwargs):
        announcements = Announcement.objects.all().order_by('-date_created')
        page_no = self.kwargs.get('page')
        paginator = Paginator(announcements, self.paginated_by)
        page = paginator.page(page_no)
        return page

class AnnouncementDetailView(DetailView):
    template_name = 'main/announcement_detail.html'
    model = Announcement
    context_object_name = "announcement"
    pk_url_kwarg = 'pk'

class AdmissionView(TemplateView):
    template_name = 'main/admissions.html'

class NewsBaseView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = 'main:news_paged'

    def get_redirect_url(self, *args, **kwargs):
        kwargs['page'] = 1
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)

class NewsListPaginate(ListView):
    template_name = 'main/news.html'
    model = News
    context_object_name = "news"
    paginated_by = 10


    def get_queryset(self, *args, **kwargs):
        news = News.objects.all().order_by('-published_date')
        page_no = self.kwargs.get('page')
        paginator = Paginator(news, self.paginated_by)
        page = paginator.page(page_no)
        return page

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



class AppliedRedirectView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = 'main:applied_science_paged'

    def get_redirect_url(self, *args, **kwargs):
        kwargs['page'] = 1
        return super().get_redirect_url(*args, **kwargs)

class AppliedListView(ListView):
    template_name = 'main/appliedScience.html'
    model = ResearchPaper
    context_object_name = "papers"
    

    def get_queryset(self):
        papers = ResearchPaper.objects.filter(category="Applied").order_by('-published_date')
        page_no = self.kwargs.get('page')
        paginator = Paginator(papers, 5)
        page = paginator.page(page_no)

        return page

class AppliedDetailView(DetailView):
    template_name = 'main/appliedScience_detail.html'
    model = ResearchPaper
    context_object_name = "applied_science_research"
    pk_url_kwarg = "pk"

class LifeRedirectView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = 'main:life_science_paged'

    def get_redirect_url(self, *args, **kwargs):
        kwargs['page'] = 1
        return super().get_redirect_url(*args, **kwargs)

class LifeListView(ListView):
    template_name = 'main/lifeScience.html'
    model = ResearchPaper
    context_object_name = "papers"
    

    def get_queryset(self):
        papers = ResearchPaper.objects.filter(category="Life").order_by('-published_date')
        page_no = self.kwargs.get('page')
        paginator = Paginator(papers, 5)
        page = paginator.page(page_no)

        return page

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
