from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('caja', views.Caja.as_view(), name='caja'),
]