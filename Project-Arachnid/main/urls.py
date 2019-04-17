from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),

    path('admissions',
        views.AdmissionView.as_view(),
        name="admissions"),

    path('news/',
        views.NewsBaseView.as_view(),
        name="news"),

    path('news/page/<int:page>', views.NewsListPaginate.as_view(), name="news_paged"),

    path('news/details/<int:pk>', views.NewsDetailView.as_view(),
        name="news_detail"),

    path('organizations',views.OrganizationListView.as_view(),name="organizations"),
    path('organizations/details/<int:pk>', views.OrganizationDetailView.as_view(), name="organization_details"),


    path('life_science', views.LifeRedirectView.as_view(), name="life_science"),
    path('life_science/page/<int:page>', views.LifeListView.as_view(), name="life_science_paged"),
    path('life_science/details/<int:pk>', views.LifeDetailView.as_view(),name="life_science_detail"),

    path('applied_science', views.AppliedRedirectView.as_view(),name="applied_science"),
    path('applied_science/page/<int:page>', views.AppliedListView.as_view(), name="applied_science_paged"),
    path('applied_science/details/<int:pk>', views.AppliedDetailView.as_view(),name="applied_science_detail"),

    path('about',
        views.AboutView.as_view(),
        name="about"
    ),

    path('faqs',
        views.FAQsView.as_view(),
        name="faqs"
    )
]
