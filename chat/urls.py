from django.urls import path

from chat.views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('choose/', index, name='index'),
    path('room/<int:pk>/', RoomView.as_view(), name='room'),
    path('logout/', do_logout, name='logout'),
]
