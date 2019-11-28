"""projectmhn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from appmhn import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('profiles/',views.profiles, name='profiles'),
    path('step/',views.step, name='step'),
    path('viewprofile/<int:id>/',views.viewprofile, name='viewprofile'),
    path('store/',views.store, name='store'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('register/', views.register, name='reg'),
    path('login/', views.login, name='in'),
    path('logout/', views.logout, name='out'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)