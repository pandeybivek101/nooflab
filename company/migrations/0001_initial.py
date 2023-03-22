# Generated by Django 4.1.7 on 2023-03-22 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessId', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('registrationDate', models.DateField()),
                ('companyForm', models.CharField(max_length=10)),
            ],
        ),
    ]
