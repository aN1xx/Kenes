from django.db.models import TextChoices


class GradeTypes(TextChoices):
    JUNIOR = 'Junior level', 'JUNIOR'
    MIDDLE = 'Middle level', 'MIDDLE'
    SENIOR = 'Senior level', 'SENIOR'
