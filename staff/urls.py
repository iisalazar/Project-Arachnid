from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('announcements/', views.AnnouncetListView.as_view(), name='announcements'),
    path('file_upload/', views.FileFieldView.as_view(), name="file_upload")
]
