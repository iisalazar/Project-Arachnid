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

    path('organizations/',
        views.OrganizationView.as_view(),
        name="organizations"),

    path('about/',
        views.AboutView.as_view(),
        name="about"
    ),

    path('faqs/',
        views.FAQsView.as_view(),
        name="faqs"
    )
]
