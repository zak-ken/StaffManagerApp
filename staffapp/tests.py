from django.test import TestCase
from django.urls import reverse
from .models import Employee


class EmployeeModelTest(TestCase):
    def test_insert_into_employees(self):
        """Inserts test users into the DB"""

        simple_data = ['Alexander', 'Programmer', '1896-05-02', 'Python Programmer']
        test_users = {'bob': simple_data, 'tom': simple_data, 'carren': simple_data, 'leo': simple_data,
                      'kathy': simple_data, 'bob marley': simple_data}
        emp = Employee()
        for i, user in enumerate(test_users):
            emp.employee_firstname = user
            emp.employee_surname = test_users[user][0]
            emp.employee_job_title = test_users[user][1]
            emp.date_started = test_users[user][2]
            emp.job_description = test_users[user][3]
            self.assertIs(emp.save(), None)


class EmployeeViewEmployeesTests(TestCase):

    def test_no_employees(self):
        """Test if the view employee page works"""
        response = self.client.get(reverse('emp:view_employees'))
        self.assertEqual(response.status_code, 200)


class EmployeesCreateEmployeeTests(TestCase):

    def test_employee_create_page(self):
        """Test if the employee create page works"""
        response = self.client.get(reverse('emp:creating_employee'))
        self.assertEqual(response.status_code, 200)
