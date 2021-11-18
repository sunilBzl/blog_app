from django.urls import path

from . import views


app_name= 'BlogApp'

urlpatterns = [
    path('', views.PostListView.as_view(), name = 'home'),
    path('blog/sports/', views.SportListView.as_view(), name = 'sports'),
    path('blog/news/', views.NewsListView.as_view(), name = 'news'),
    path('blog/music/', views.MusicListView.as_view(), name = 'music'),
    path('about/', views.aboutus, name='aboutus'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]