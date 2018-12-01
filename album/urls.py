from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('', views.AlbumTemplateView.as_view(), name="albums"),
    path('lists/', views.AlbumList.as_view(), name="albums_list"),
    path('photos/list', views.PhotoList.as_view(), name="photos_list")
]
