from django.urls import include
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('', include('apps.mentors.urls')),
]
