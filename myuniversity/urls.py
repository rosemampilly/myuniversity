from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from register.views import Home
from myuniversity.views import anonymous_required
from register import urls as reg_urls


urlpatterns = [
    # Examples:
    # url(r'^$', 'myuniversity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^register/', include(reg_urls)),
    url(r'^admin/', include(admin.site.urls)),
     url(r'^user/login/$', anonymous_required(auth_views.login),
        {'template_name': 'login.html'},name='login'),

     url(r'^user/logout/$',
        auth_views.logout,
        {'template_name': 'logout.html'},
        name='logout'),
]