from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Notes_list, name='Notes_list'),
    url(r'^notes/(?P<pk>\d+)/$',views.Notes_detail,name='Notes_detail'),
]