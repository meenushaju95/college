from django.db import models

from django.contrib.auth.models import User




# Create your models here.
class Course(models.Model):
    Course_name=models.CharField(max_length=255)
    course_fee=models.IntegerField()
class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    Student_name=models.CharField(max_length=255)
    Student_address=models.CharField(max_length=255)
    Student_age=models.IntegerField()
    Joining_date=models.DateField()
class Usermember(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    userr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Adress=models.CharField(max_length=255)
    Age=models.IntegerField()
    Contact=models.CharField(max_length=255)
    Image=models.ImageField(blank=True,upload_to="image/",null=True)



# Create your models here.
