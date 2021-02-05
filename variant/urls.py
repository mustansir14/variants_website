from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="variants-home"),
    path("home/", views.home, name="variants-home"),
    path("about/", views.about, name="variants-about"),
    path("contact/", views.contact, name="variants-contact"),
    path("search/", views.search, name="variants-search"),
    path("search/advanced/", views.advanced_search, name="variants-advanced-search"),
    path("<str:gene>/<str:variant>/", views.detail, name="variants-detail")
]
