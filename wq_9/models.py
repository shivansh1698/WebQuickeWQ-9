from django.db import models



class Registration(models.Model):
    Name = models.CharField(max_length = 200)
    Email = models.CharField(max_length = 200)
    Phone = models.CharField(max_length = 20)
    Qualification  = models.CharField(max_length = 30)
    InterestedCourse = models.CharField(max_length= 30)

    

