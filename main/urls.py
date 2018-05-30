from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('admissions/',
        views.AdmissionView.as_view(),
        name="admissions"),

    path('news/',
        views.NewsView.as_view(),
        name="news"),

    path('news/details/<int:pk>/', views.NewsDetailView.as_view(),
        name="news_detail"),

    path('organizations/',
        views.OrganizationView.as_view(),
        name="organizations"),

    path('life_science/', views.LifeListView.as_view(), name="life_science"),
    path('life_science/details/<int:pk>/', views.LifeDetailView.as_view(),name="life_science_detail"),

    path('applied_science/', views.AppliedListView.as_view(),name="applied_science"),
    path('applied_science/details/<int:pk>/', views.AppliedDetailView.as_view(),name="applied_science_detail"),


    path('about/',
        views.AboutView.as_view(),
        name="about"
    ),

    path('faqs/',
        views.FAQsView.as_view(),
        name="faqs"
    )
]
