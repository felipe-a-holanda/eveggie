from django.db import models
from autoslug import AutoSlugField


class Town(models.Model):
    name = models.CharField(max_length=100)

    slug = AutoSlugField(max_length=120, db_index=True, populate_from='name')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(max_length=120, db_index=True, populate_from='name')
    desc = models.CharField(max_length=1000)
    address = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/', blank=True, null=True)

    town = models.ForeignKey(Town)

    STARS = ((1, 'one'),
             (2, 'two'),
             (3, 'three'),
             (4, 'four'),
             (5, 'five'))
    votes = models.IntegerField(choices=STARS, default=3)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name





class Ingredient(models.Model):
    name = models.CharField(max_length=120, db_index=True)
    slug = AutoSlugField(max_length=120, db_index=True, populate_from='name')

    picture = models.ImageField(upload_to='images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="products")
    name = models.CharField(max_length=120, db_index=True)
    slug = AutoSlugField(max_length=120, db_index=True, populate_from='name')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering=('name', )
        index_together = (('id', 'slug'), )
        verbose_name = 'product'

    def __str__(self):
        return self.name
