from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import FileFieldForm
from .models import FileUpload


class IndexView(ListView):
    model = FileUpload
    template_name = 'staff/index.html'
    context_object_name = 'files'
    def get_queryset(self):
        return FileUpload.objects.all

class AnnouncetListView(ListView):
    model = FileUpload
    template_name = 'staff/announcements.html'
    context_object_name = 'files'
    def get_queryset(self):
        return FileUpload.objects.all

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'staff/upload.html'  # Replace with your template.
    success_url = reverse_lazy('staff:announcements')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            file = FileUpload(file=request.FILES['file'])
            file.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
