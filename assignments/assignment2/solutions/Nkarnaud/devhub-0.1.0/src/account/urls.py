from django.urls import path
from django.conf.urls import url
from account import views as core_views


urlpatterns = [
    url('index/', core_views.index, name='index'),
    url(r'^signup/$', core_views.signup, name='signup'),
]
