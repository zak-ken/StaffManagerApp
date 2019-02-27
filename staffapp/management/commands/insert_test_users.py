from django.core.management.base import BaseCommand
from staffapp.models import Employee


class Command(BaseCommand):
    args = ''
    help = 'test users insertion'

    def handle(self, *args, **options):
        simple_data = ['Alexander', 'Programmer', '1896-05-02', 'Python Programmer']
        test_users = {'bob': simple_data, 'tom': simple_data, 'carren': simple_data, 'leo': simple_data,
                      'kathy': simple_data, 'marley': simple_data, 'sam': simple_data, 'io': simple_data}

        for user in test_users:
            emp = Employee()
            emp.employee_firstname = user
            emp.employee_surname = test_users[user][0]
            emp.employee_job_title = test_users[user][1]
            emp.date_started = test_users[user][2]
            emp.job_description = test_users[user][3]
            emp.save()

        print('Test Users Insert, Complete....')
