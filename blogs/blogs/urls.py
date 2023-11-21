from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from blog.views import *

urlpatterns = [
    path('', first_page, name="first_page"),
    path('add_post/', add_post, name="add_post"),
    path('check_post/<int:id_post>/', like_post, name='check_post'),
    path('admin/', admin.site.urls),
    path('delete_post/<int:id_post>/', delete_post, name='delete_post'),
    path('login/', PageLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
