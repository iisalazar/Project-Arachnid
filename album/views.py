from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.views import View
from django.http import JsonResponse # For the image view
from django.contrib.auth.mixins import LoginRequiredMixin # For authentication
from .forms import PhotoForm, AlbumForm
from .models import Photo, Album
from pprint import pprint
from django.core import serializers
import json

import os # For returning the appropriate file name, not the directory + filename
# Create your views here.


# For the public

class AlbumTemplateView(TemplateView):
    template_name = 'album/albums.html'

class AlbumList(View):
    def get(self, *args, **kwargs):
        albums = Album.objects.order_by('-date')
        data = []
        for album in albums:
            alb = {}
            photo = get_list_or_404(Photo, album=album)
            alb['name'] = album.title
            alb['slug'] = album.slug
            alb['date_created'] = album.date
            alb['description'] = album.description
            alb['first_photo'] = photo[0].file.url
            data.append(alb)

        print(data)
        #pprint(json.dumps(albums_serialized))
        return JsonResponse({'data' : data})

class PhotoList(View):
    def get(self, *args, **kwargs):
        photos = get_list_or_404(Photo)
        data = []
        for photo in photos:
            image = {}
            image['album'] = photo.album.pk
            image['file'] = photo.file.url
            image['date'] = photo.date
            data.append(image)
        pprint(data)
        return JsonResponse({'data': data})
        #return ("Hello world")

# For the admin panel
class AlbumCreateView(LoginRequiredMixin, CreateView):
    template_name = 'album/album_create.html'
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('staff:albums')

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('staff:albums')

class AlbumListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'album/albums.html'

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
        data = {'album_slug': album.slug, 'photos': album.photos.all()}
        return data

class PhotoUploadView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        photoForm = PhotoForm(self.request.POST, self.request.FILES)
        if photoForm.is_valid():
            photo = photoForm.save(commit=False)
            album = get_object_or_404(Album, slug=self.kwargs.get('album'))
            photo.album = album
            photo.save()
            data = {'is_valid': True, 'url' : photo.file.url, 'name' : os.path.split(photo.file.name)[1] }
        else:
            data = {'is_valid' : False}

        return JsonResponse(data)

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    pk_url_kwarg = 'pk'
    url = ''
    success_url = reverse_lazy('staff:albums') ## TODO: change the returned url
                                                # and redirect back to the
                                                # photos page
    def delete(self, *args, **kwargs):
        print("O oh!! someone deleted a photo")
        return super().delete(*args, **kwargs)
