from django.urls import path

from account import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'login/', views.login),
    path(r'register/', views.register)

]
