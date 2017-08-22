from django.conf.urls import url
from BoiBye2017 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^comment/new/$', views.comment_new, name='comment_new'),
]
