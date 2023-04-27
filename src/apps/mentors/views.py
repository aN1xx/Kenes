from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from rest_framework import generics, mixins
from django_filters import rest_framework as filters

from .models import Mentor
from .serializers import MentorSerializer
from .filters import MentorFilter


def index(request):
    return render(request, 'index.html')


def sign_in(request):
    return render(request, 'SignIn.html')


def sign_up(request):
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