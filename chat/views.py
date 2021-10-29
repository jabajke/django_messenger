from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse

from .models import RoomModel

from rest_framework.views import APIView


class LoginView(APIView):

    def post(self, request):
        print(request.user)
        if not request.user.is_authenticated:
            get_user_model().objects.create_user(**request.data)
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            login(request, user)
        return HttpResponseRedirect(reverse('index'))


def index(request):
    room = request.GET.get('room')
    return render(request, 'chat/index.html', {"room": room})


class RoomView(APIView):

    def post(self, request):
        username = request.data['username']
        room = request.data['room']
        if RoomModel.objects.filter(title=room).first():
            return render(request, 'chat/room.html', {"username": username,
                                                      "room": room})
        return redirect('index')


def do_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
