from django.urls import path
from tasks import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
