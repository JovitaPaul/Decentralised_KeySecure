from django.urls import path
from . import views

urlpatterns = [
    path('upload-key/', views.upload_key, name='upload_key'),
]
