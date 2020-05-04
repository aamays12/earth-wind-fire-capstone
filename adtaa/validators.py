from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_1to4(value):
    if value < 0 or value > 4:
        raise ValidationError(
            _('%(value)s is not between 1 and 4 inclusive'),
            params={'value': value},
        )
