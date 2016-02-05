from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from register.views import Home

urlpatterns = (
    # Examples:
    # url(r'^$', 'myuniversity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
