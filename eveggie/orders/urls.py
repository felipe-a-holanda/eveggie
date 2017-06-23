from django.conf.urls import url

from . import views

urlpatterns = [


    url(
        regex=r'^add/(?P<restaurant_slug>[\w.@+-]+)/(?P<pk>\d+)/$',
        view=views.orderItem,
        name='order'
    ),
    url(
        regex=r'^remove/(?P<restaurant_slug>[\w.@+-]+)/(?P<pk>\d+)/$',
        view=views.removeItem,
        name='remove'
    ),
]
