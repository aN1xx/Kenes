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