import json
from sqlite3 import IntegrityError

from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, mixins
from django_filters import rest_framework as filters

from .models import Mentor, Booking
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
            Mentor.objects.create(user=user)

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
    # mentor = Mentor.objects.get(user=request.user)
    # if request.method == 'POST':
    #     try:
    #         mentor.save(update_fields=['full_name', 'gender', 'location'])
    #     except Exception as e:
    #         print(f"Couldn't save the data: {e}")
    return render(request, 'MentorsStep13.html')


def mentor_14(request):
    # mentor = Mentor.objects.get(user=request.user)
    # if request.method == 'POST':
    #     mentor.full_name = request.POST['prompt1']
    #     mentor.gender = request.POST['options4']
    #     mentor.location = f"{request.POST['option112'], request.POST['option10']}"
    #     try:
    #         mentor.save(update_fields=['full_name', 'gender', 'location'])
    #     except Exception as e:
    #         print(f"Couldn't save the data: {e}")
    return render(request, 'MentorsStep14.html')


def mentor_141(request):
    return render(request, 'MentorsStep141.html')


@login_required
def dashboard(request):
    mentor = Mentor.objects.get(user=request.user)
    data = {
        'full_name': mentor.full_name,
        'image': str(mentor.profile_picture).replace('src/', ''),
    }
    return render(request, 'dashboard.html', data)


def landing_page_after(request):
    return render(request, 'LandingPageAfter.html')


@login_required
def my_profile(request):
    mentor = Mentor.objects.get(user=request.user)
    table_data = [
        ['9 AM', '', '', '', '', '', '', '', '', '', ''],
        ['12 AM', '', '', '', '', '', '', '', '', '', ''],
        ['3 PM', '', '', '', '', '', '', '', '', '', ''],
        ['5 PM', '', '', '', '', '', '', '', '', '', ''],
        ['7 PM', '', '', '', '', '', '', '', '', '', ''],
    ]
    booked = []
    data = {
        'full_name': mentor.full_name,
        'about': mentor.about,
        'occupation': mentor.occupation,
        'grade': mentor.grade,
        'experience': mentor.experience,
        'image': str(mentor.profile_picture).replace('src/', ''),
        'table_data': table_data,
    }
    if request.method == 'POST':
        button_value = request.POST.get('button_value')
        if 'AM' in button_value:
            slot_time = button_value.replace(' AM', ':00')
        else:
            int_time = int(button_value[0]) + 12
            slot_time = str(int_time) + ':00'

        _, booking = Booking.objects.get_or_create(user=request.user, slot_date=timezone.now().date(), slot_time=slot_time)
        print(f"SUCCESSFULLY BOOKED: {booking}")
        return render(request, 'myprofile.html', data)

    return render(request, 'myprofile.html', data)


@login_required
def other_profile(request):
    return render(request, 'otherprofile.html')


def search(request):
    mentors = Mentor.objects.all()
    for i in mentors:
        i.profile_picture = str(i.profile_picture).replace('src/', '')

    data = {'mentors': mentors}
    return render(request, 'SearchResults.html', data)
