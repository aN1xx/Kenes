# Generated by Django 3.2.15 on 2023-06-04 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0003_mentor_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='grade',
            field=models.CharField(choices=[('Junior level', 'JUNIOR'), ('Middle level', 'MIDDLE'), ('Senior level', 'SENIOR')], max_length=100, null=True),
        ),
    ]