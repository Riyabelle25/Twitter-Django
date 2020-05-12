from django.db import models

# Create your models here.


# model for User 
class User(models.Model):

  name = models.CharField(max_length=120)
  
  def __str__(self):
        return self.name

class Tweet(models.Model):

    tweet = models.CharField(max_length=120)
    user = models.ForeignKey('User', related_name='tweets',on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet, self.user