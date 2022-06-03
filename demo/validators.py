from django.core.exceptions import ValidationError


def is_even(number):
    if number % 2 == 0:
        raise ValidationError('%(number)s is even number', params={'number': number})
