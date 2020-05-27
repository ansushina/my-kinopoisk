"""mycourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from coureser import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.IndexView.as_view(), name="index"),
                  path('film/<int:pk>/', views.FilmView.as_view(), name='film'),
                  path('login/', views.LoginView.as_view(), name='login'),
                  path('register/', views.RegisterView.as_view(), name='register'),
                  path('logout/', views.LogoutView.as_view(), name='logout'),
                  path('settings/', views.SettingsView.as_view(), name='settings'),
                  path('search/', views.SearchView.as_view(), name='search'),
                  path('like/<int:pk>/', views.LikeView.as_view(), name='like'),
              ] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
