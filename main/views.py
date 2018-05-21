from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'main/index.html'

class AdmissionView(TemplateView):
    template_name = 'main/admissions.html'

class NewsView(TemplateView):
    template_name = 'main/news.html'

class OrganizationView(TemplateView):
    template_name = 'main/orgs.html'

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
