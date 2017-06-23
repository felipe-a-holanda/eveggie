from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^(?P<slug>[\w.@+-]+)$',
        view=views.ReviewListView.as_view(),
        name='list'
    ),
]
