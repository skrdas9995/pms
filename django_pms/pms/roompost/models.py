from django.db import models

# Create your models here.

class DoctorDetails(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    specialist = models.CharField(max_length=200)
    mobile = models.IntegerField()
    biography = models.CharField(max_length=200)
    dob = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    bloodgroup =models.CharField(max_length=200)
    status =models.BooleanField(max_length=200)
    # photo = models.CharField(max_length=200)

    class Meta:
        db_table= 'Doctors_details'

