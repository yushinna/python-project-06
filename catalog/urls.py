from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'random', views.random_mineral, name='random'),
    url(r'mineral/(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
    url(r'', views.mineral_list, name='index'),
]
