from django.urls import path, include
from . import views, admin
from hello.views import secret_page


urlpatterns = [
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contripb.auth.urls')),
    path('secret_page/', secret_page, name='secret_page'),
]