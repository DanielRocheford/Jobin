from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=0)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=50, null=True)
    school = models.CharField(max_length=100, null=True)
    program = models.CharField(max_length=100, null=True)
    major = models.CharField(max_length=100, null=True)
    graduate = models.BooleanField(default=False)
    gender = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=30, null=True)

    def get_absolute_url(self):
        return reverse('student:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.firstname + ' ' + self.lastname
