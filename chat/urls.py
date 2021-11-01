from django.urls import path

from chat.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('room/<str:room_name>/', room, name='room'),
    path('room-redirect/', room_redirect, name='room_redirect'),
    path('logout/', do_logout, name='logout'),
]
