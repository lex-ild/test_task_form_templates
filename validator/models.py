from enum import Enum

from django.db import models


class DataType(Enum):
    EMAIL = 'email'
    PHONE = 'phone'
    DATE = 'date'
    TEXT = 'text'


class FormTemplate(models.Model):
    name = models.CharField(max_length=100)

    form_data: dict[str, str] = models.JSONField(default=dict)
