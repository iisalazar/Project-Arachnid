from django.urls import path, include
from . import views
from album import views as album_views
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

    path('research/', views.ResearchListView.as_view(), name="research"),
    path('research/create/', views.ResearchCreateView.as_view(), name="create_research"),
    path('research/delete/<int:pk>/', views.ResearchDeleteView.as_view(), name="delete_research"),
    path("research/update/<int:pk>/", views.ResearchUpdateView.as_view(), name="update_research"),
    path("research/details/<int:pk>/", views.ResearchDetailView.as_view(), name="research_detail"),
    path('research/details/<int:pk>/add_proponent/', views.add_proponent_to_research, name="add_proponent_to_research"),

    path('accounts/login/', auth_view.login, name="login"),
    path('accounts/logout/', auth_view.logout, name="logout", kwargs={'next_page': '/'}),

    # For the organization hr
    path('organizations/<organization>/hr/', views.OrganizationHRListView.as_view(), name="organization_hr_list"),
    path('organizations/<organization>/hr/create', views.OrganizationHRCreateView.as_view(), name="organization_hr_create"),
    path('organizations/<organization>/hr/delete/<int:pk>/', views.OrganizationHRDeleteView.as_view(), name="organization_hr_delete"),
    path('organizations/<organization>/hr/update/<int:pk>/', views.OrganizationHRUpdateView.as_view(), name="organization_hr_update"),
    path('organizations/<organization>/hr/details/<int:pk>/', views.OrganizationHRDetailView.as_view(), name="organization_hr_detail"),

    # for the albums section
    path('albums/', album_views.AlbumListView.as_view(), name="albums"),
    path('albums/create', album_views.AlbumCreateView.as_view(), name="create_album"),
    path('albums/<slug:album>/photos/delete/<int:pk>/', album_views.PhotoDeleteView.as_view(), name="delete_photo"),
    path('albums/<slug:album>/photos', album_views.PhotosListView.as_view(), name="photos"),
    path('albums/<slug:album>/photos/upload', album_views.PhotoUploadView.as_view(), name="upload_photo")

]
