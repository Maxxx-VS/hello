from django.urls import path, include
from . import views
from django.contrib import admin
from hello.views import secret_page



urlpatterns = [
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret_page/', secret_page, name='secret_page'),
]