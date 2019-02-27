==========
management
==========

The staff management is a simple Django app to perform crud commands on employees.

steps:
-----
# Steps are incoherent, do not follow, need to rewrite


    1. This web-app requires django 2.0 and python 3.5.

    3. No DB settings is needed as sqlite3 is used by default.

    2. create a virtual env.
        -> python3 -m venv vp or virtualenv -p python3.5 venv

    3. Activate vp and run "pip install -e staffmanager_package"

    4. Create a project, "django-admin startproject staffmanager"

    5.
        * Add "staffapp.apps.StaffAppConfig" to your INSTALLED_APPS setting like this:

            INSTALLED_APPS = [
                'staffapp.apps.StaffAppConfig',
                ...
            ]

        * Add the following settings in your settings.py
            -> MEDIA_URL = '/media/'
            -> MEDIA_ROOT = os.path.join(BASE_DIR, 'staffapp/media')

    6. Include the following into URLconf in your project urls.py like this::

        from django.urls import path, include
        from django.contrib import admin
        from django.conf import settings
        from django.conf.urls.static import static
        from staffmanager import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', views.redirect_employee),
            path('staff_management', views.redirect_employee),
            path('staff_management/', include('staffapp.urls')),
        ]

        if settings.DEBUG:
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    7. create a views.py in your project and add the following:

        from django.shortcuts import redirect, reverse

        def redirect_employee(request):
            """
            :param request:
            :return: Redirects the user to a valid page
            """
            return redirect(reverse('emp:view_employees'))

    8. Run `python manage.py makemigrattions`.

    9. Run `python manage.py migrate` to create the employee models.

    10. Run `python manage.py insert_test_users` to create the forecast models.

    11. Visit http://127.0.0.1:8000 to view the site.
