from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

app_name = 'staff'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('announcements/', views.AnnouncementListView.as_view(), name='announcements'),
    path('announcements/create/', views.AnnouncementCreateView.as_view(), name="create_announcement"),
    path('announcements/view/<int:pk>/', views.view_file, name="view_file"),

    path('news/', views.NewsListView.as_view(), name="news"),
    path('news/create/', views.NewsCreateView.as_view(), name="create_news"),
    path('news/update/<int:pk>/', views.NewsUpdateView.as_view(), name="update_news"),
    path('news/delete/<int:pk>/', views.NewsDeleteView.as_view(), name="delete_news"),
    path('news/publish/<int:pk>/', views.publish_news, name="publish"),

    path('organizations/', views.OrganizationListView.as_view(), name="organizations"),
    path('organizations/create/', views.OrganizationCreateView.as_view(), name="create_organization"),
    path('organizations/delete/<int:pk>/', views.OrganizationDeleteView.as_view(), name="delete_organization"),
    path('organizations/update/<int:pk>/', views.OrganizationUpdateView.as_view(), name="update_organization"),
    path('organization/details/<int:pk>/', views.OrganizationDetailView.as_view(), name="organization_detail"),

    path('accounts/login/', auth_view.login, name="login"),
    path('accounts/logout/', auth_view.logout, name="logout", kwargs={'next_page': '/'})
]
