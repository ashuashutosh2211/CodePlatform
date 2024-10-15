from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True) 
    cf_handle = models.CharField(max_length=50, unique=True)  
    password = models.CharField(max_length=128 , null = True , blank=True)
    email_id = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.cf_handle