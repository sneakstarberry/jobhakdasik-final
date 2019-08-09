from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name='detail'),
    path('new/', views.newcreate  , name="newcreate"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('delcomment/<int:pk>', views.del_comment, name="del_comment"),
    path('comment/<int:pk>', views.add_comment, name='add_comment'),
    path('editcomment/<int:pk>', views.edit_comment, name= 'edit_comment'),
    path('search', views.search, name="search"),
    path('post_home/', views.post_home, name="post_home"),
    path('like/<int:blog_id>', views.like, name="like"),
    path('favorite/<int:blog_id>', views.favorite, name="favorite")
]
