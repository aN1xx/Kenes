from django.contrib import admin

from apps.mentors.models import Mentor


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'about', 'occupation']
    search_fields = [
        'id',
        'first_name',
        'last_name',
        'middle_name',
        'about',
        'occupation',
        'grade',
        'created_at',
    ]
    ordering = ('-created_at',)

    @admin.display(description='ФИО')
    def full_name(self, obj):
        return obj.full_name
