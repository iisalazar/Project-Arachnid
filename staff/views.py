from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import AnnouncementForm
from .models import Announcement
from django.contrib.auth.mixins import LoginRequiredMixin
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


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

@login_required
def view_file(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(announcement.file)

    p = canvas.Canvas(response)
    p.showPage()
    p.save()
    return response