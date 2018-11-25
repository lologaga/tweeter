from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=264, unique=True)
    name = models.CharField(max_length=264)
    bio = models.CharField(max_length=1500)

    def __repr__(self):
        return "<User {}>".format(self.name)

    def __str__(self):
        return self.user_name

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(pattern='%m-%d-%Y')
    text = models.CharField(max_length=140)


    def __repr__(self):
        return "<Tweet {}>".format(self.text)

    def __str__(self):
        return self.text


