# Generated by Django 3.0.3 on 2020-02-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('specialist', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('biography', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('bloodgroup', models.CharField(max_length=20)),
                ('status', models.BooleanField(max_length=20)),
                ('photo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Doctors_details',
            },
        ),
    ]