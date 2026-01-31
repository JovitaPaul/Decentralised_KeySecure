from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('get-file/', views.get_file, name='get_file'),  # <-- new line
]
