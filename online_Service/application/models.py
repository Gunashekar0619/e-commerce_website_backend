from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    type = models.CharField(max_length=20, blank=False)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)

    gender = models.CharField (max_length=10,blank=True)

    #def __str__(self):
     #   return self.User.username


class Goods(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, null= True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    price = models.IntegerField()
    comments = models.CharField(max_length=100, blank=True)



    def no_of_ratings(self):
        rating = Ratings.objects.filter(good=self)
        l = len(rating)
        return l

    def avg_ratings(self):
        sum = 0
        rating = Ratings.objects.filter(good=self)
        l = len(rating)
        for rating in rating:
            sum += rating.stars
        if l > 0:
            return sum / l
        else:
            return 0


class Ratings(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'good'),)
        index_together = (('user', 'good'),)