import uuid
import iuliia

from django.db import models

from apps.common.utils import KAZ_TRANSLITERATION


class UUIDPKModel(models.Model):
    id: uuid.UUID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class CharIDModel(models.Model):
    id = models.CharField('Уникальный код', max_length=127, primary_key=True)
    verbose_name = models.CharField('Название', max_length=255, null=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return str(self.verbose_name)


class FullNameModel(models.Model):
    first_name: str = models.CharField(
        verbose_name='Имя',
        max_length=150,
        null=True,
        blank=True,
    )
    last_name: str = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        null=True,
        blank=True,
    )
    middle_name: str = models.CharField(  # TODO change to patronymic name
        verbose_name='Отчество',
        max_length=150,
        default='',
        blank=True,
    )

    class Meta:
        abstract = True

    @property
    def full_name(self) -> str:
        return ' '.join([i for i in [self.last_name, self.first_name, self.middle_name] if i])

    @property
    def first_name_latin(self) -> str:
        return iuliia.translate(self.first_name or '', KAZ_TRANSLITERATION).upper()

    @property
    def middle_name_latin(self) -> str:
        return iuliia.translate(self.middle_name or '', KAZ_TRANSLITERATION).upper()

    @property
    def last_name_latin(self) -> str:
        return iuliia.translate(self.last_name or '', KAZ_TRANSLITERATION).upper()

    def save(self, *args, **kwargs):
        if not self.middle_name:
            self.middle_name = ''
        super().save(*args, **kwargs)
