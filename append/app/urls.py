from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='blog-details'),
    path('services/', views.services, name='services-details'),
    path('blog/', views.blog, name='blog'),
    path('portfolio-details/', views.portfolio, name='portfolio-details'),
]
