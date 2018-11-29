from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views import View
from django.http import JsonResponse # For the image view
from django.contrib.auth.mixins import LoginRequiredMixin # For authentication
from .forms import PhotoForm, AlbumForm
from .models import Photo, Album
# Create your views here.

class AlbumListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'album/albums.html'
    template_name = 'album/albums.html'
    model = Album
    context_object_name = 'albums'
    def get_queryset(self):
        return Album.objects.order_by('-date')

class PhotosListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'album/albums.html'
    template_name = 'album/photo_list.html'
    model = Photo
    context_object_name = 'photos'
    def get_queryset(self):
        album = get_object_or_404(Album, slug=self.kwargs.get('album'))
        data = {'album': album.title, 'photos': album.photos.all()}
        return data

class PhotoUploadView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        photoForm = PhotoForm(self.request.POST, self.request.FILES)
        if photoForm.is_valid():
            photo = photoForm.save(commit=False)
            album = get_object_or_404(Album, slug=self.kwargs.get('album'))
            photo.album = album
            photo.save()
            data = {'is_valid': True, 'url' : photo.file.url, 'name' : photo.file.name }
        else:
            data = {'is_valid' : False}

        return JsonResponse(data)

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    pass