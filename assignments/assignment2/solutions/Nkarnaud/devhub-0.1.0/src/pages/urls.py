from django.conf.urls import url
from pages import views as pages_view

urlpatterns = [
    url('', pages_view.HomeView.as_view(), name='home'),
]