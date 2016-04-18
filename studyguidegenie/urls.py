"""studyguidegenie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
"""mysite URL Configuration

[...]
"""

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'', include('guide.urls')),
    url(r'^$','account.views.home_view', name='home'),
    url(r'^account/register/$', 'account.views.register_view',name='register'),
    url(r'^account/login/$', 'account.views.login_view',name='login'),
    url(r'^account/logout/$', 'account.views.logout_view',name='logout'),
    url(r'^guide/login$', 'account.views.landing_view',name='index'),
    # url(r'^homepage/$', TemplateView.as_view(template_name='guide/homepage.html'),name='homepage'),
    # url(r'^home/$',TemplateView.as_view(template_name='guide/home.html'),name='home'),
    # # url(r'^$', 'guide.views.home', name='home'),
    # url(r'^about/$',TemplateView.as_view(template_name='guide/about.html'),name='about'),
    # url(r'^signin/$',TemplateView.as_view(template_name='guide/signin.html'),name='signin'),
    # url(r'^base2/',TemplateView.as_view(template_name='guide/base2.html'),name='base2'),
    # url(r'^contact/$',TemplateView.as_view(template_name='guide/contact.html'),name='contact'),
    # url(r'^notes$', TemplateView.as_view(template_name='guide/Notes_list.html'), name='Notes_list'),
    # url(r'^notes/(?P<pk>\d+)/$',TemplateView.as_view(template_name='guide/Notes_detail.html'),name='Notes_detail'),
]