from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

app_name = 'staff'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('announcements/', views.AnnouncementListView.as_view(), name='announcements'),
    path('announcements/create/', views.AnnouncementCreateView.as_view(), name="create_announcement"),
    path('announcements/view/<int:pk>/', views.view_file, name="view_file"),
    path('accounts/login/', auth_view.login, name="login"),
    path('accounts/logout/', auth_view.logout, name="logout", kwargs={'next_page': '/'})
]
