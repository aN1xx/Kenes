from django.db.models import TextChoices


class GradeTypes(TextChoices):
    JUNIOR = 'JUNIOR', 'Junior level'
    MIDDLE = 'MIDDLE', 'Middle level'
    SENIOR = 'SENIOR', 'Senior level'
