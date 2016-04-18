from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    #url(r'^$', 'guide.views.home', name='home'),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^about/$',TemplateView.as_view(template_name='about.html'),name='about'),
    #url(r'^contact/$',TemplateView.as_view(template_name='contact.html'),name='contact'),
    #url(r'^$',TemplateView.as_view(template_name='Notes_list.html'),name='Notes_list'),
    #url(r'^notes/(?P<pk>\d+)/$',TemplateView.as_view(template_name='Notes_detail.html'),name='Notes_detail'),
    # url(r'^$', views.Notes_list, name='Notes_list'),
    # url(r'^notes/(?P<pk>\d+)/$',views.Notes_detail,name='Notes_detail'),
]