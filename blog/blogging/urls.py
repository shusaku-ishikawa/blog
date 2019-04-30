
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

app_name = 'blogging'
urlpatterns = [
    path('', views.PostList.as_view(), name = 'post_list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name = 'post_detail'), 
]
