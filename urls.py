from django.urls import path
from . import views

# app_name = 'hello'

urlpatterns = [
    # path('', views.index_photo, name='index_photo'),
    # path('upload/', views.upload_photo, name='upload_photo'),
    path('register/', views.register, name='register' ),
]