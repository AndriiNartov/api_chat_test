import re

from django.core.validators import RegexValidator


content_text_validation_regex = re.compile(r'^(?=.{1,99}$)')
CONTENT_TEXT_LENGTH_VALIDATOR = RegexValidator(
    regex=content_text_validation_regex,
    message='Message text must be from 1 to 100 characters.'
)

email_validation_regex = re.compile(
    r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9!#$%&'*+/=?^._`{|}~-]{1,64}(?<!\.)"
    r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)
EMAIL_VALIDATOR = RegexValidator(
    regex=email_validation_regex,
    message='Please, check if your email is correct.'
)
