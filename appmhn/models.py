from django.db import models

class Age(models.Model):
    age=models.CharField(max_length=20)
    def __str__(self):
        return self.age


class Hero(models.Model):
    firstname=models.CharField(max_length=20)
    secondname=models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField()
    gender = models.CharField(max_length=20)
    age = models.ForeignKey(Age,on_delete=models.CASCADE)
    hobbies = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    photo = models.FileField(upload_to='pics/')
    text=models.CharField(max_length=20)


