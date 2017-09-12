from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rplist1, name='rplist1'),
]