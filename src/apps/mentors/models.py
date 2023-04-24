import uuid

from django.db import models

from apps.common import models as common_models
from apps.mentors import GradeTypes


class Mentor(
    common_models.UUIDPKModel,
    common_models.FullNameModel,
    common_models.TimestampedModel,
):
    id: uuid.UUID

    about: str = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    occupation: str = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    grade: str = models.CharField(
        max_length=100,
        choices=GradeTypes.choices,
        blank=False,
        null=True,
    )

    description: str = models.TextField(
        max_length=300,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return ' {}'.format(
            ' '.join([i for i in [self.last_name, self.first_name, self.middle_name] if i]),
        )
