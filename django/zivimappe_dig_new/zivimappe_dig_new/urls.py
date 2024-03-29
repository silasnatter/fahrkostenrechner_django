"""zivimappe_dig_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import stat
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user import views as user_views
from user.views import PostListView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('register/', user_views.register, name="register"),
    path('post/<int:pk>/', user_views.post_detail, name='post-detail'),
    path('image_view/<int:pk>/', user_views.image_view, name='image_view'),
    path('create_post/', user_views.create_post, name="create_post"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
