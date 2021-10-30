from django.urls import path

from chat.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('room/<str:room_name>/', room, name='room'),
    path('logout/', do_logout, name='logout'),
]
