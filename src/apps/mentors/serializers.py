from rest_framework import serializers
from .models import Mentor


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'created_at',
            'updated_at',
            'about',
            'occupation',
            'grade',
            'description',
        ]
