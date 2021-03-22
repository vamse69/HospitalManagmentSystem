# Generated by Django 3.0.4 on 2021-03-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Data',
            fields=[
                ('Patient_name', models.CharField(max_length=50)),
                ('Patient_Department', models.CharField(max_length=50)),
                ('Patient_Id_No', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Patient_mobile', models.IntegerField()),
                ('doc_address', models.TextField(max_length=200)),
                ('doc_email', models.EmailField(default=None, max_length=254)),
            ],
        ),
    ]
