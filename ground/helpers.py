from django.conf import settings
from .models import Customer
def get_customer(user: settings.AUTH_USER_MODEL):
    # pprint(list(Customer.objects.all()))
    return Customer.objects.filter(user_id=user.id).first()


def get_user(customer: Customer):
    return settings.AUTH_USER_MODEL.objects.filter(customer_set_id=customer.id).first()

