from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from allaccess.views import OAuthRedirect

from mysite import views
from .views import home 

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")), 
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^login/(?P<provider>(\w|-)+)/$', views.AdditionalPermissionsRedirect.as_view(), name='flogin'),
#    url(r'^accounts/profile/(?P<provider>)', views.FloginCallback.as_view(), name='fflogin'),
#    url(r'^associate/(?P<provider>(\w|-)+)/$', login_required(views.AssociateRedirect.as_view()), name='associate'),
#    url(r'^associate-callback/(?P<provider>(\w|-)+)/$', login_required(views.AssociateCallback.as_view()), name='associate-callback'),
    url(r'^accounts/', include('allaccess.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^$', home, name='home'),
)
