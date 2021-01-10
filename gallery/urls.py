from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'$',views.gallery_today,name='galleryToday'),
]