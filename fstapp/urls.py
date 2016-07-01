from django.conf.urls import include, url
from django.contrib import admin
from fstmobile import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'fstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/$', views.ListContacts.as_view()),

]
