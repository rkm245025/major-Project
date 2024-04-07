from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("login",views.login_view,name="login"),
    path("contactus",views.contactus,name="contactus"),
    path("registration",views.registration,name="registration"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("home",views.home,name="home"),
    path("saveform",views.saveform,name="saveform"),
    path("loginin",views.loginin,name="loginin"),
    path("parent",views.parent,name='parent')

]