from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('mentee-1/', views.mentee_1, name='mentee-1'),
    path('mentee-13/', views.mentee_13, name='mentee-13'),
    path('mentee-14/', views.mentee_14, name='mentee-14'),
    path('choose-a-role/', views.choose_a_role, name='choose-a-role'),
    path('mentee-9/', views.mentee_9, name='mentee-9'),
    path('mentee-10/', views.mentee_10, name='mentee-10'),
    path('mentee-11/', views.mentee_11, name='mentee-11'),
    path('mentee-12/', views.mentee_12, name='mentee-12'),
    path('mentee-15/', views.mentee_15, name='mentee-15'),
    path('mentor-8/', views.mentor_8, name='mentor-8'),
    path('mentor-9/', views.mentor_9, name='mentor-9'),
    path('mentor-10/', views.mentor_10, name='mentor-10'),
    path('mentor-11/', views.mentor_11, name='mentor-11'),
    path('mentor-12/', views.mentor_12, name='mentor-12'),
    path('mentor-13/', views.mentor_13, name='mentor-13'),
    path('mentor-14/', views.mentor_14, name='mentor-14'),
    path('mentor-141/', views.mentor_141, name='mentor-141'),
]
