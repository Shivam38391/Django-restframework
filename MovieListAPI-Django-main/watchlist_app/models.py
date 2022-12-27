from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField( max_length=200)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    plateform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE , related_name="watchlist") #related for reverse action
    avg_rating = models.FloatField(default=0)
    number_of_ratings = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    watchlist = models.ForeignKey(Watchlist , on_delete=models.CASCADE , related_name="reviews")
    description = models.CharField(max_length=150, null=True)
    created = models.DateTimeField(auto_now_add=True) #this add time when firstime was created
    update = models.DateTimeField(auto_now=True) # update time everytime updated
    active = models.BooleanField(default=True) 


    def __str__(self):
        return str(self.rating) + " | " + str(self.watchlist.title)

