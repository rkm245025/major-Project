from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.contrib import messages
from student.models import Enquiry,Registration,Login
from . models import Program,Branch,Year,Material,News
from datetime import datetime
from stundentlogin.views import StuResponce
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    return render(request,"adminhome.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminlogout(request):
    try:
        del request.session['adminid']
        messages.success(request,"admin logoutsuccesfully")
        return redirect(reverse("login"))
    
    
    except KeyError:
        return redirect("login")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewenquiry(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            enq=Enquiry.objects.all()
            return render(request,"viewenquiry.html",locals())
    except KeyError:
            return redirect("login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
def viewstudent(request):
    try:
          
        if request.session['adminid']!=None:
             adminid=request.session['adminid']
             stu=Registration.objects.all()
             return render(request,"viewstundent.html",locals())
    except KeyError:
        return redirect('login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
def uploadstudy(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            if request.method=="POST":

                program=request.POST['program']
                branch=request.POST['branch']
                year=request.POST['year']
                subject=request.POST['subject']
                filename=request.POST['filename']
                myfile=request.FILES['myfile']
                mt=Material(program=program,branch=branch,year=year,subject=subject,filename=filename,myfile=myfile)
                mt.save()
                return render(request,"uploadstudy.html",locals())

    except KeyError:
      return redirect('login')

    #return render(request,"uploadstudy.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def move(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            program=Program.objects.all()
            branch=Branch.objects.all()
            year=Year.objects.all()
            return render(request,'uploadstudy.html',locals())
    except KeyError:
        return redirect('login')
    #return render(request,'uploadstudy.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudy(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            mat=Material.objects.all()
            return render(request,'uploadstudymaterial.html',locals())
    except KeyError:
        return redirect('login')
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changeadminpass(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            log=Login.objects.get(userid=adminid)
            if request.method=="POST":
                oldpassword=request.POST['oldpassword']
                newpassord=request.POST['newpassword']
                confirmpassword=request.POST['confirmpassword']
                if oldpassword==log.password:
                    if oldpassword!=newpassord:
                        if newpassord==confirmpassword:
                            Login.objects.filter(userid=adminid).update(password=newpassord)
                            return redirect('adminlogout')
                        else:
                            messages.error(request,"confirm password not match")
                    else:
                        messages.error("password not same as previos password")
                else:
                    messages.error(request,"login password do not matchs")


            #messages.success(request,"password change succesfully")
            return render(request,'changeadminpassword.html',locals())

    except KeyError:
        return redirect('login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def news(request):
   try:
       
   
    if request.session['adminid']!=None:
         adminid=request.session['adminid']
         if request.method =="POST":
             newstitle=request.POST["newstitle"]
             newstext=request.POST['newstext']
             newsby=request.POST['newsby']
             newsdate=datetime.today()
             notice=News(newstitle=newstitle,newstext=newstext,newsby=newsby,newsdate=newsdate)
             notice.save()
             messages.success(request,'notice Upload successfully')
         return render(request,'news.html')
   
   except KeyError:
       return redirect('login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcomplain(request):
    try:

        if request.session['adminid']!=None:
            #try
            adminid=request.session['adminid']
            comp=StuResponce.objects.filter(responcetype='complain')
            return render(request,"viewcomplain.html",locals())
        
    except KeyError:
        return redirect('login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)   
def viewfeedback(request):
    if request.session['adminid']!=None:
        adminid =request.session['adminid']
        feed=StuResponce.objects.filter(responcetype='feedback')
        return render(request,'viewfeedback.html',locals())
    

#def admin(request):
 #   return render(request,'index.html')