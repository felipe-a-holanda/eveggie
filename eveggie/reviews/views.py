from django.shortcuts import render

from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from .models import Review
from restaurants.models import Restaurant


class ReviewListView(ListView):

    model = Review


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ReviewListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['restaurant'] = Restaurant.objects.get(slug=self.kwargs['slug'])
        return context


    def get_queryset(self):

        return Review.objects.filter(restaurant__slug=self.kwargs['slug'])
    # These next two lines tell the view to index lookups by username


