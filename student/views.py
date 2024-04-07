from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from datetime import date
from .models import Registration, Login,Enquiry
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from  adminapp import *
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from  adminapp.models import Program,Branch,Year
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    
    return render(request, "student/home.html")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def home(request):
    return render(request, "student/home.html")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def registration(request):
    year=Year.objects.all()
    branch=Branch.objects.all()
    return render(request, "student/registration.html",locals())
@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def login_view(request):
    '''if request.method == "POST":
        userid = request.POST["userid"]
        password = request.POST["password"]
        usertype = request.POST["usertype"]

        try:
            # Replace 'YourUserModel' with the actual name of your User model
            obj = Login.objects.get(userid=userid, password=password, usertype=usertype)
            
            if obj.usertype == "student":
                user = authenticate(username=userid,password=password)
                
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                  messages.error(request, "Authentication failed")
            else:
                messages.error(request, "Invalid user type")
        except Login.DoesNotExist:
            messages.error(request, "Invalid credentials")'''
    try:
         

        return render(request, "student/login.html")
    except KeyError:
         return redirect("login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def contactus(request):
    if request.method=="POST":
        name=request.POST["name"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        email=request.POST['email']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        enq=Enquiry(name=name,gender=gender,address=address,email=email,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        messages.success(request,"We will contact you soon thank you ")


    return render(request, "student/contactus.html")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def aboutus(request):
    return render(request, "student/aboutus.html")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def saveform(request):
    message = ""
    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]
        fname = request.POST["fname"]
        branch = request.POST["branch"]
        year = request.POST["year"]
        address = request.POST["address"]
        aadhar = request.POST["aadhar"]
        email = request.POST["email"]
        regdate = date.today()
        password = request.POST["password"]
        usertype = "student"
        
        
        reg = Registration(
            username=username, name=name, dob=dob, gender=gender,
            fname=fname, branch=branch, year=year, address=address,
            aadhar=aadhar, email=email, regdate=regdate
        )
        
        log = Login(
            userid=username, password=password, usertype=usertype,
        )
        
        reg.save()
        log.save()
        
        year=Year.objects.all()
        branch=Branch.objects.all()
        subject="Registration"
        msg=f'hi {username} you Registerd Succesfully and id is {username}  and Password is {password}'
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[email,]
        send_mail(subject=subject,message=msg,from_email=email_from,recipient_list=recipient_list)
        messages.success(request, 'Your Registration is Successfull.')


        return render(request,'student/registration.html',locals())

    return render(request, "student/registration.html", {'message': message})



@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def loginin(request):
    
        if request.method == "POST":
            userid = request.POST["userid"]
            password = request.POST["password"]
            usertype = request.POST["usertype"]
        try:
            obj=Login.objects.get(userid=userid,password=password,usertype=usertype)
            if obj.usertype=="student":
                    request.session["username"]=userid

                    stu=Registration.objects.get(username=userid)
            #user=authenticate(username=userid,password=password)
            #if user is not None:
             #   login(request,user)
                    return redirect(reverse("studenthome"),{"stu":stu})

            elif obj.usertype=="admin":
                    request.session["adminid"]=userid
                    return redirect(reverse('adminhome'))
            else:
                    messages.error(request,"invalid credencial")
                    messages.error(request,f"{userid} {password}",{usertype})
                    return redirect('login')
        except :
                messages.error(request,"invalid user")
                return render(request,"student/login.html")
        #return render(request,"student/login.html")

        
def parent(request):
     return render(request,'student/parent.html')