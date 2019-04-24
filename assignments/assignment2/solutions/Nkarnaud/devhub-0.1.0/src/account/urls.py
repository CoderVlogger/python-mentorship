from django.conf.urls import url
from account import views as account_views

urlpatterns = [
    url('signup/', account_views.SignupView.as_view(), name='signup'),
]
