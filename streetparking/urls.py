from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('detail/', views.detail, name = 'index'),
    path('results/', views.results, name = 'index')
]