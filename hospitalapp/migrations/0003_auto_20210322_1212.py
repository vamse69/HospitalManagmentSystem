# Generated by Django 3.0.4 on 2021-03-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_patient_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_data',
            old_name='doc_address',
            new_name='Patient_address',
        ),
        migrations.RemoveField(
            model_name='patient_data',
            name='doc_email',
        ),
        migrations.AddField(
            model_name='patient_data',
            name='Patient_email',
            field=models.EmailField(default=False, max_length=254),
        ),
        migrations.AlterField(
            model_name='doctors_data',
            name='doc_email',
            field=models.EmailField(default=False, max_length=254),
        ),
        migrations.AlterField(
            model_name='doctors_data',
            name='doc_present_working_status',
            field=models.BooleanField(default=False),
        ),
    ]
