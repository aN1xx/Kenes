import json
from sqlite3 import IntegrityError

from django.contrib.auth import authenticate, login, get_user_model
from django.http import JsonResponse
from django.shortcuts import render, redirect
from drf_spectacular.utils import extend_schema
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, mixins
from django_filters import rest_framework as filters

from .models import Mentor
from .serializers import MentorSerializer
from .filters import MentorFilter
from ..users.models import User


User = get_user_model()

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'SignIn.html', {'error_message': error_message})

    else:
        return render(request, 'SignIn.html')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, password=password)

        except Exception:
            error_message = "This username is taken"
            return render(request, 'SignUp.html', {'error_message': error_message})

        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('/choose-a-role/')
        else:
            # Show an error message
            error_message = "This username is taken"
            return render(request, 'SignUp.html', {'error_message': error_message})
    else:
        return render(request, 'SignUp.html')


def mentee_1(request):
    return render(request, 'MenteesStep1.html')


def mentee_14(request):
    return render(request, 'MenteesStep14.html')


def mentee_13(request):
    return render(request, 'MenteesStep13.html')


def choose_a_role(request):
    return render(request, 'ChooseARole.html')


def mentee_9(request):
    return render(request, 'MenteesStep9.html')


def mentee_10(request):
    return render(request, 'MenteesStep10.html')


def mentee_11(request):
    return render(request, 'MenteesStep11.html')


def mentee_12(request):
    return render(request, 'MenteesStep12.html')


def mentee_15(request):
    return render(request, 'MenteesStep15.html')


def mentor_8(request):
    return render(request, 'MentorsStep8.html')


def mentor_9(request):
    return render(request, 'MentorsStep9.html')


def mentor_10(request):
    return render(request, 'MentorsStep10.html')


def mentor_11(request):
    return render(request, 'MentorsStep11.html')


def mentor_12(request):
    return render(request, 'MentorsStep12.html')


def mentor_13(request):
    return render(request, 'MentorsStep13.html')


def mentor_14(request):
    return render(request, 'MentorsStep14.html')


def mentor_141(request):
    return render(request, 'MentorsStep141.html')


def dashboard(request):
    return render(request, 'Dashboard.html')
