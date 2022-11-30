from django.urls import path

from hostel_management_app import views

urlpatterns=[
    path("",views.home,name="home"),
    path("index",views.index,name="index"),
    path("index1",views.index1,name="index1"),
    path("login",views.login,name="login"),

]