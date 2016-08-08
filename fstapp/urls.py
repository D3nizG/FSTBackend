from django.conf.urls import include, url
from django.contrib import admin
from fstmobile import views

urlpatterns = [
    # Examples:

    # url(r'^blog/', include('blog.urls')),

    url(r'^$','fstmobile.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/$', views.ListContacts.as_view()),
    url(r'^faqs/$', views.ListFAQs.as_view()),
    url(r'^news/$', views.ListNews.as_view()),
    url(r'^scholarship/$', views.ListScholarship.as_view()),
    url(r'^places/$', views.ListPlaces.as_view()),
    url(r'^events/$',views.ListEvents.as_view()),
    url(r'^images/$',views.ListImages.as_view()),
    
]
