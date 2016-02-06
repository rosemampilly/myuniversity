from django.conf.urls import include, url
from register.views import *
from
from

urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='signup'),
    url(r'^dash/$', UserDashboardView.as_view(), name='dash'),
    url(r'^success/$', UserRegistrationSuccessView.as_view(), name='signup_success')
        ]