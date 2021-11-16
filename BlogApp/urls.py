from django.urls import path

from . import views


app_name= 'BlogApp'

urlpatterns = [
    path('', views.PostListView.as_view(), name = 'home'),
    # path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]