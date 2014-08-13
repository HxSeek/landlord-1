from datetime import timedelta

from django.utils import timezone


def generate_date_list():
    date_list = []
    now = timezone.localtime(timezone.now())
    date_of_this_Monday = now - timedelta(days=now.weekday())
    for i in range(0, 7):
        date_list.append(date_of_this_Monday + timedelta(days=i))
    return date_list


def get_application_this_week(model):
    ''' get all applications whose applied field
    is going to be used this week '''
    now = timezone.localtime(timezone.now())
    date_of_this_Monday = now - timedelta(days=now.weekday())
    date_of_next_Monday = date_of_this_Monday + timedelta(days=7)
    application_this_week = model.objects.filter(
        date__gte=date_of_this_Monday,
        date__lt=date_of_next_Monday,
        deleted=False)
    return application_this_week
