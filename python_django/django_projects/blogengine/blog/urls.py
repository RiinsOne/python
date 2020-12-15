from django.urls import path

from .views import *

# some-title


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url')
]
