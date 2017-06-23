from django.shortcuts import render

from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from .models import Restaurant
from orders.models import Order

class RestaurantDetailView(DetailView):
    model = Restaurant
    # These next two lines tell the view to index lookups by username
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RestaurantDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['order'] = Order.objects.first()
        return context



class RestaurantListView(ListView):
    model = Restaurant
    # These next two lines tell the view to index lookups by username


