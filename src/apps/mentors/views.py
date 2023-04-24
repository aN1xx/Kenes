from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from rest_framework import generics, mixins
from django_filters import rest_framework as filters

from .models import Mentor
from .serializers import MentorSerializer
from .filters import MentorFilter


@extend_schema(
    responses=MentorSerializer,
    description='Search API description',
)
class MentorSearchAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = MentorFilter
