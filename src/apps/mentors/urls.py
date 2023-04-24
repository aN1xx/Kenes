from django.urls import path

from . import views


urlpatterns = [
    path(
        'search/',
        views.MentorSearchAPIView.as_view(),
    ),
]
