from django.conf import settings
from .models import Customer
from datetime import datetime
from pprint import pprint

from templated_mail.mail import BaseEmailMessage
from django.core.mail import BadHeaderError


def get_customer(user: settings.AUTH_USER_MODEL):
    # pprint(Customer.objects.filter(user_id=user.id))
    return Customer.objects.filter(user_id=user.id).first()
