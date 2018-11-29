from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('', views.AlbumListView.as_view(), name="albums"),
    path('<slug:album>/photos', views.PhotosListView.as_view(), name="photos"),
    path('<slug:album/photos/delete/<int:pk>/', views.PhotoDeleteView.as_view(), name="delete_photo"),
    path('<slug:album>/photos/upload', views.PhotoUploadView.as_view(), name="upload_photo")
]
