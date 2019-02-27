from django.db import models
from django.db.models.deletion import Collector
from django.db import router
from .common.util.system_operations import delete_image


class Employee(models.Model):
    employee_firstname = models.CharField(max_length=20, blank=False, unique=True)
    employee_surname = models.CharField(max_length=20, blank=False)
    employee_job_title = models.CharField(max_length=20, blank=False)
    date_started = models.DateField('Date started at Company', blank=False)
    job_description = models.TextField(max_length=70, default=None)
    employee_image = models.ImageField(upload_to="employee_images/", blank=True)

    def delete(self, using=None, keep_parents=False):

        if self.employee_image:
            image_url = self.employee_image.url
            image_path = image_url[image_url.find('/', 2):]
            delete_image(image_path=image_path)

        return super().delete(using, keep_parents)


