from django.urls import path
from . import views
#app_name='adminapp'
urlpatterns=[
   # path("index",views.index,name="index"),
    path("stundentlogout",views.stundentlogout,name="stundentlogout"),
    path("viewprofile",views.viewprofile,name="viewprofile"),
    path("viewstudymaterialstundent",views.viewstudymaterialstundent,name="viewstudymaterialstundent"),
    path("studenthome",views.studenthome,name="studenthome"),

    path('viewnews',views.viewnews,name="viewnews"),
    path('postquestion',views.postquestion,name="postquestion"),
    path('postanswer/<qid>',views.postanswer,name='postanswer'),
    path('viewanswer/<qid>',views.viewanswer,name="viewanswer"),
    path('postans',views.postans,name="postans"),
    path('changestupass',views.changestupass,name='changestupass'),
    path('feedback',views.feedback,name='feedback'),

    
]