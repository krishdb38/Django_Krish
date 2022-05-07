from django.urls import path
from my_app.views import indexView, postFriend

urlpatterns = [
    path('', indexView),
    path('post/ajax/friend', postFriend , name = 'post_friend')
]