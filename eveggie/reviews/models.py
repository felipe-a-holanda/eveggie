from django.db import models

from django.db import models
from restaurants.models import Restaurant
from eveggie.users.models import User



class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='reviews')
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=1000)

    STARS = ((1, 'one'),
             (2, 'two'),
             (3, 'three'),
             (4, 'four'),
             (5, 'five'))

    quality = models.IntegerField(choices=STARS, default=3)
    price = models.IntegerField(choices=STARS, default=3)
    punctuality = models.IntegerField(choices=STARS, default=3)
    service = models.IntegerField(choices=STARS, default=3)

    overall = models.IntegerField(choices=STARS, default=3)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
