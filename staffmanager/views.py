from django.shortcuts import redirect, reverse


def redirect_employee(request):
    """
    :param request:
    :return: Redirects the user to a valid page
    """
    return redirect(reverse('emp:view_employees'))
