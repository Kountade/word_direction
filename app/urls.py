from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('', views.home, name='home-page'),
    path('politiques', views.politique, name='politique-page'),
    path('sports', views.sports, name='sports-page'),
    path('bussness', views.business, name='bussness-page'),
    path('blogs', views.blogsene, name='blogs-page'),
    path('blogdetails/<str:title>', views.blog_detail, name="blogdetail"),
    path('home/<path:news_title>/',
         views.home_detail, name='home_detail'),
    path('politique/<path:news_title>/',
         views.politique_detail, name='politique_detail'),
    path('sport/<path:news_title>/',
         views.sports_detail, name='sport_detail'),
  
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
