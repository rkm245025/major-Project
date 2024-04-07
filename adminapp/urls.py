from django.urls import path
from . import views

urlpatterns=[
    path("",views.adminhome,name="adminhome"),
    path("adminlogout",views.adminlogout,name="adminlogout"),
    path("viewenquiry",views.viewenquiry,name="viewenquiry"),
    path("viewstudent",views.viewstudent,name="viewstudent"),
    path("uploadstudy",views.uploadstudy,name='uploadstudy'),
    path('move',views.move,name="move"),
    path('viewstudy',views.viewstudy,name="viewstudy"),
    path('changeadminpassword',views.changeadminpass,name="changeadminpassword"),
    path('news',views.news,name='news'),
    path('viewcomplain',views.viewcomplain,name="viewcomplain"),
    path('viewfeedback',views.viewfeedback,name="viewfeedback"),
    #path('admin',views.admin,name='admin')


]
