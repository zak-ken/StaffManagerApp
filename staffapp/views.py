from django.views.generic import CreateView, UpdateView, ListView
from staffapp.forms import EmployeeForm
from staffapp.models import Employee
from django.http import JsonResponse


class ViewEmployees(ListView):
    template_name = 'employees/employees.html'
    context_object_name = 'staff_members'

    def get_queryset(self):
        return Employee.objects.all()


class CreateEmployee(CreateView):
    template_name = 'employees/employee_edit_form.html'
    form_class = EmployeeForm
    success_url = '/staff_management/employees/view'


class UpdateEmployee(UpdateView):
    template_name = 'employees/employee_edit_form.html'
    form_class = EmployeeForm
    success_url = '/staff_management/employees/view'

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `pk` argument in the URLconf.
        """
        obj = Employee.objects.get(pk=self.kwargs.get(self.pk_url_kwarg))
        return obj


def delete_employee(request):
    """
    :param request: Used to retrieve the id of the employee to be deleted
    :return: returns a Json response on whether the deletion was a success or failure
    """
    action_id = request.POST.get('param_data[id]')
    try:
        result = Employee.objects.get(pk=action_id).delete()
    except Exception as e:
        print('Error: ', e)
        result = False
    return JsonResponse({'user_delete': result})
