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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from coureser.views.FilmView import FilmView
from coureser.views.IndexView import IndexView
from coureser.views.LikeView import LikeView
from coureser.views.LoginView import LoginView
from coureser.views.LogoutView import LogoutView
from coureser.views.RegisterView import RegisterView
from coureser.views.SearchView import SearchView
from coureser.views.SettingsView import SettingsView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', IndexView.as_view(), name="index"),
                  path('film/<int:pk>/', FilmView.as_view(), name='film'),
                  path('login/', LoginView.as_view(), name='login'),
                  path('register/', RegisterView.as_view(), name='register'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('settings/', SettingsView.as_view(), name='settings'),
                  path('search/', SearchView.as_view(), name='search'),
                  path('like/<int:pk>/', LikeView.as_view(), name='like'),
              ] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
