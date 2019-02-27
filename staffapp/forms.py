from staffapp.models import Employee
import datetime
from django.utils import timezone
from django import forms
from .common.util.system_operations import delete_image


class EmployeeForm(forms.ModelForm):

    def clean(self):
        cd = super().clean()
        prev_image = self.instance.employee_image
        if 'employee_image' in cd:
            if (cd['employee_image'] is False and prev_image) or (cd['employee_image'] and prev_image):
                image_url = prev_image.url
                image_url = image_url[image_url.find('/', 2):]
                delete_image(image_path=image_url)

        future = timezone.now() + datetime.timedelta(days=1)
        date = cd.get('date_started')
        if str(date) >= str(future):
            self.add_error('date_started', "The date started value cannot be in the future! ...")
        return cd

    class Meta:
        model = Employee
        exclude = ()
