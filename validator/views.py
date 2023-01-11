import re
from typing import Any

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FormTemplate, DataType


VALID_EMAIL = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
VALID_PHONE = re.compile(r"^[\s][7][\s][0-9]{3}[\s][0-9]{3}[\s][0-9]{2}[\s][0-9]{2}$")
VALID_DATE = re.compile(
    r"^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$"
)
VALID_OTHER_DATE = re.compile(
    r"\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])*"
)


@api_view(['POST'])
def find_form_template(request) -> dict[str: str]:
    data: dict[str, Any] = request.query_params.dict()

    parsed_form_data: dict = {}
    returned_form_data: dict = {}

    for key, value in data.items():
        data_type = find_data_type(value)
        parsed_form_data[f'form_data__{key}'] = data_type.value

        returned_form_data[key] = data_type.value

    template = FormTemplate.objects.filter(
        **parsed_form_data
    ).first()

    if template:
        result_data = {
            'name': template.name,
        }
    else:
        result_data = returned_form_data

    return Response(data=result_data)


def find_data_type(value: str) -> DataType:
    if VALID_EMAIL.match(value):
        return DataType.EMAIL
    if VALID_PHONE.match(value):
        return DataType.PHONE
    if VALID_DATE.match(value) or VALID_OTHER_DATE.match(value):
        return DataType.DATE
    return DataType.TEXT
