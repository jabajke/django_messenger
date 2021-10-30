from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse

from .models import RoomModel, Message

from rest_framework.views import APIView


class LoginView(APIView):

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            login(request, user)
        if not request.user.is_authenticated:
            create = get_user_model().objects.create_user(**request.data)
            login(request, create)
        return HttpResponseRedirect(reverse('index'))


def index(request):
    user = request.user
    rooms = RoomModel.objects.all()
    return render(request, 'chat/index.html', {"room": rooms, "user": user})


def room(request, room_name):
    print(room_name)
    username = request.user
    message = Message.objects.filter(room=room_name)[0:25]
    return render(request, 'chat/room.html', {"username": username, "room_name": room_name,
                                              "message": message})



def do_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
