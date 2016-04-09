from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from mvhbc import views

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.home, name='home'),



    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', views.about, name='about'),
    url(r'^resources/', views.resources, name='resources'),
    url(r'^competition/', include('competition.urls')),
    url(r'^accounts/login/', RedirectView.as_view(pattern_name='login')),

    #url(r'^$', views.membership, name='membership'),
    #url(r'^$', views.officers, name='officers'),
)