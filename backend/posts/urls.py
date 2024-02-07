from django.urls import path
from . import api

urlpatterns = [
    path('', api.post_list, name='posts_list'),
    path('create/', api.create_post, name='create_post'),
]