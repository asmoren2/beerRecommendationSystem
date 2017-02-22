from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /beer/
    url(r'^beer$', views.beer_list, name='beer_list'),
    # ex: /beer/5/
    url(r'^beer/(?P<beer_id>[0-9]+)/$', views.beer_detail, name='beer_detail'),
]
