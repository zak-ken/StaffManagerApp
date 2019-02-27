# Generated by Django 2.0 on 2018-01-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffapp', '0002_auto_20180123_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_started',
            field=models.DateTimeField(verbose_name='Date started at Company'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_firstname',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_job_title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_surname',
            field=models.CharField(max_length=20),
        ),
    ]
