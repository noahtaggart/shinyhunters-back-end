"""app_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app_api.views import register_user, login_user
from rest_framework import routers
from django.conf.urls import include
from app_api.views import PokeApiView, HuntView, TrainerView, UserView, PhotoView, PokemonView, MethodView, GameView
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'pokes', PokeApiView, 'poke')
router.register(r'hunts', HuntView, 'hunt')
router.register(r'trainers', TrainerView, 'trainer')
router.register(r'users', UserView, 'user')
router.register(r'photos', PhotoView, 'photo')
router.register(r'pokemon', PokemonView, 'pokemon')
router.register(r'methods', MethodView, 'method')
router.register(r'games', GameView, 'game')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
