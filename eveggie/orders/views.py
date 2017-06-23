from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Order, Item
from restaurants.models import Product


def orderItem(request, pk, restaurant_slug):
    order, created = Order.objects.get_or_create()
    product = Product.objects.get(pk=pk)
    item, created = Item.objects.get_or_create(order=order, product=product, price=product.price)
    if not created:
        item.quantity += 1
        item.save()
    return HttpResponseRedirect(reverse('restaurants:detail', args=[restaurant_slug]))



def removeItem(request, pk, restaurant_slug):
    order, created = Order.objects.get_or_create()

    item = Item.objects.get(pk=pk)
    if not created:
        item.quantity -= 1
        item.save()
        if item.quantity ==0:
            item.delete()
    return HttpResponseRedirect(reverse('restaurants:detail', args=[restaurant_slug]))
