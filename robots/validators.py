# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
# import datetime
# import re
#
# pattern = '^[A-Za-z0-9]*$'
# datetime_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
#
#
# def validate_json_data(data):
#     if not re.match(pattern, data['model']) or not re.match(pattern, data['version']):
#         raise ValidationError(
#             _(f"Model and version should be only digit and letters {data['model']},{data['version']} s"),
#             params={
#                 'pattern': pattern,
#                 "model": data['model'],
#                 "version": data['version']
#             },
#         )
#     if not len(data['model']) == 2:
#         raise ValidationError(
#             f"Length model:{data['model']} can`t be  more than two"
#         )
#     if not len(data['version']) == 2:
#         raise ValidationError(
#             f"Length version:{data['version']} can`t be  more than two"
#         )
#     if not re.match(datetime_pattern, data['created']):
#         raise ValidationError(
#             _("Created should be  'YYYY-MM-DD HH:MM:SS' format %(created)"),
#             params={
#                 "created": data['created'],
#             }
#         )
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
import re

pattern = '^[A-Za-z0-9]*$'
datetime_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'


def validate_json_data(data):
    errors = []

    if not re.match(pattern, data['model']) or not re.match(pattern, data['version']):
        errors.append(
            ValidationError(
                _(f"Model and version should be only digits and letters: {data['model']}, {data['version']}"),
                params={
                    'pattern': pattern,
                    "model": data['model'],
                    "version": data['version']
                },
            )
        )

    if not len(data['model']) == 2:
        errors.append(
            ValidationError(
                f"Length model: {data['model']} can't be more than two"
            )
        )

    if not len(data['version']) == 2:
        errors.append(
            ValidationError(
                f"Length version: {data['version']} can't be more than two"
            )
        )

    if not re.match(datetime_pattern, data['created']):
        errors.append(
            ValidationError(
                _("Created should be in 'YYYY-MM-DD HH:MM:SS' format: %(created)s"),
                params={
                    "created": data['created'],
                }
            )
        )

    if errors:
        raise ValidationError(errors)

