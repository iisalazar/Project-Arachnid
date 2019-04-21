from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView, FormView
from django.urls import reverse_lazy, reverse

from announcements.forms import AnnouncementForm
from news.forms import NewsForm
from organizations.forms import OrganizationForm, OrganizationHRForm
from research.forms import ResearchForm, ResearchProponentForm


from announcements.models import Announcement
from news.models import News
from organizations.models import Organization, OrganizationOfficer
from research.models import ResearchPaper, ResearchProponent

# from .forms import AnnouncementForm, NewsForm, OrganizationForm, ResearchForm, ResearchProponentForm, OrganizationHRForm
# from .models import Announcement, News, Organization, ResearchPaper, ResearchProponent, OrganizationOfficer
from django.contrib.auth.mixins import LoginRequiredMixin
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect


class IndexView(LoginRequiredMixin, TemplateView):
    redirect_field_name='staff/index.html'
    template_name = 'staff/index.html'

class AnnouncementListView(LoginRequiredMixin, ListView):
    redirect_field_name='staff/index.html'
    model = Announcement
    context_object_name= 'announcements'
    def get_queryset(self):
        return Announcement.objects.order_by('-date_created')

class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name='staff/index.html'
    model = Announcement
    form_class = AnnouncementForm

class AnnouncementUpdateView(LoginRequiredMixin, UpdateView):
    redirect_filed_name = 'staff/announcement_list.html'
    model = Announcement
    form_class = AnnouncementForm
    pk_url_kwargs = 'pk'

class AnnouncementDeleteView(LoginRequiredMixin, DeleteView):
    model = Announcement
    success_url = reverse_lazy('staff:announcements')
    pk_url_kwarg = 'pk'

class AnnouncementDetailView(LoginRequiredMixin, DetailView):
    model = Announcement
    context_object_name = 'announcement'
    pk_url_kwarg = 'pk'


def view_file(request, pk):
    from arachnid.settings import BASE_DIR
    announcement = get_object_or_404(Announcement, pk=pk)
    file = BASE_DIR + announcement.file.url
    f = open(file, 'w+b')
    f.seek(0)
    pdf = f.read()
    f.close()
    return HttpResponse(file, 'application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(announcement.file)

    #p = canvas.Canvas(response)
    #p.showPage()
    #p.save()
    #return response

# ------------------- News Views ------------------- #

class NewsListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'staff/index.html'
    model = News
    context_object_name = "news"
    def get_queryset(self):
        return News.objects.order_by('-created_date')

class NewsCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = 'staff/news_list.html'
    model = News
    form_class = NewsForm

class NewsUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = 'staff/news_list.html'
    model = News
    form_class = NewsForm
    pk_url_kwarg = 'pk'

class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('staff:news')

@login_required
def publish_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.publish()
    return redirect('staff:index')


# ------------------- Organization Views ------------------- #

class OrganizationListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'staff/index.html'
    model = Organization
    context_object_name = 'organizations'
    def get_queryset(self):
        return Organization.objects.order_by('name')

class OrganizationCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = 'staff/index.html'
    model = Organization
    form_class = OrganizationForm

class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = 'staff/index.html'
    model = Organization
    form_class = OrganizationForm
    pk_url_kwarg = 'pk'

class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organization
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('staff:organizations')

class OrganizationDetailView(LoginRequiredMixin, DetailView):
    model = Organization
    context_object_name = "organization"
    pk_url_kwarg = 'pk'

# ----------- For the organization officers --------- #

class OrganizationHRListView(LoginRequiredMixin, ListView):
    template_name = 'organizations/organization_hr_list.html'
    redirect_field_name = 'staff/index.html'
    model = OrganizationOfficer
    context_object_name = 'human_resource'
    def get_queryset(self):
        organization = get_object_or_404(Organization, name=self.kwargs.get('organization'))
        print(organization.id)
        return organization.officers.all()

class OrganizationHRCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = 'staff/index.html'
    template_name = 'organizations/organization_hr_form.html'
    model = OrganizationOfficer
    form_class = OrganizationHRForm
    success_url = reverse_lazy('staff:organizations')
    def form_valid(self, form):
        organization = get_object_or_404(Organization, name=self.kwargs.get('organization'))
        officer = form.save(commit=False)
        officer.organization = organization
        officer.save()
        return HttpResponseRedirect(reverse('staff:organizations'))


class OrganizationHRUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = 'staff/index.html'
    template_name = 'organizations/organization_hr_form.html'
    model = OrganizationOfficer
    form_class = OrganizationHRForm
    pk_url_kwarg = 'pk'

class OrganizationHRDeleteView(LoginRequiredMixin, DeleteView):
    model = OrganizationOfficer
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('staff:organizations')

class OrganizationHRDetailView(LoginRequiredMixin, DetailView):
    template_name = 'organizations/organization_hr_detail.html'
    model = OrganizationOfficer
    context_object_name = "organization"
    pk_url_kwarg = 'pk'


# ------------------- Research Views ------------------- #

class ResearchListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'staff/index.html'
    model = ResearchPaper
    context_object_name = "research_papers"
    def get_queryset(self):
        return ResearchPaper.objects.order_by('-title')

class ResearchCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = 'staff/index.html'
    model = ResearchPaper
    form_class = ResearchForm

class ResearchUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = 'staff/index.html'
    model = ResearchPaper
    form_class = ResearchForm
    pk_url_kwarg = 'pk'

class ResearchDeleteView(LoginRequiredMixin, DeleteView):
    model = ResearchPaper
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('staff:research')

class ResearchDetailView(LoginRequiredMixin, DetailView):
    model = ResearchPaper
    context_object_name = 'research_paper'
    pk_url_kwarg = 'pk'

@login_required
def add_proponent_to_research(request, pk):
    research_paper = get_object_or_404(ResearchPaper, pk=pk)
    if request.method == "POST":
        form = ResearchProponentForm(request.POST)
        if form.is_valid():
            proponent = form.save(commit=False)
            proponent.research = research_paper
            proponent.save()
            return redirect('staff:research_detail', pk=research_paper.pk)
    else:
        form = ResearchProponentForm()
        return render(request, 'staff/researchpaperproponents_form.html', {'form': form})
