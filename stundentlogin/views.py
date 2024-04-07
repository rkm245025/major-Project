from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.cache import cache_control
from student.models import Registration,Login
from adminapp.models import News,Material
from datetime import date
from .models import Question,Answer,StuResponce

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def studenthome(request):
    try:
        if request.session['username']!=None:
            username=request.session['username']
            stu=Registration.objects.get(username=username)
            return render(request,"studenthome.html",{'stu':stu})
    except KeyError:
        return redirect('login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def stundentlogout(request):
    try:
        del request.session['username']
        messages.success(request,"student logout succesfully")
        return redirect("login")
    
    
    except KeyError:
        return redirect("login")
    
    



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewprofile(request):
    try:
        if request.session['username']!=None:
            username=request.session['username']
            stu=Registration.objects.get(username=username)
            log=Login.objects.get(userid=username)
            return render(request,"viewprofile.html",{'stu':stu,"log":log})
    except KeyError:
        return redirect("login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudymaterialstundent(request):
    if request.session['username']!=None:
        username=request.session['username']
        stu=Registration.objects.get(username=username)
        study=Material.objects.filter(branch=stu.branch,year=stu.year)
        return render(request,"viewstudymaterial.html",locals())
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewnews(request):
    if request.session['username']!=None:
        username=request.session['username']
        note=News.objects.all()
        return render(request,"viewnews.html",locals())
@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
def postquestion(request):
    try:
        if request.session['username']!=None:
            username=request.session['username']
            stu=Registration.objects.get(username=username)
            if request.method=="POST":
                question=request.POST['question']
                postedby=stu.name
                posteddate=date.today()
                qn=Question(question=question,postedby=postedby,posteddate=posteddate)
                qn.save()
            qn=Question.objects.all()

            return render(request,"postquestion.html",{'stu':stu,'qn':qn}) 

    except KeyError:
        return redirect('login')
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postanswer(request,qid):
    if request.session['username']!=None:
        username=request.session['username']
        stu=Registration.objects.get(username=username)

        return render(request,'postanswer.html',{'stu':stu,'qid':qid})
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewanswer(request,qid):
    try:
        if request.session['username']!=None:
            username=request.session['username']
            stu=Registration.objects.get(username=username)
            ans=Answer.objects.filter(qid=qid)
            return render(request,"viewanswer.html",{'stu':stu,'ans':ans})
    except KeyError:

        return redirect("login")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postans(request):
    if request.session['username']!=None:
            username=request.session['username']
            stu=Registration.objects.get(username=username)
            #if request.method=="POST":

            #ans=Answer.objects.filter(qid=qid)
            qid=request.POST['qid']
            answer=request.POST['answer']
            answerby=stu.name
            postedate=date.today()
            ans=Answer(answer=answer,answerby=answerby,postedate=postedate,qid=qid)
            ans.save()
            return redirect("postquestion")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changestupass(request):
    #return HttpResponse("change stu")
    if request.session['username']!=None:
        username=request.session['username']
        stu=Registration.objects.get(username=username)
        if request.method=="POST":
            oldpassword=request.POST['oldpassword']
            newpasssword=request.POST['newpassword']
            confirmpassword=request.POST['confirmpassword']
            prepass=Login.objects.get(userid=username)
            if oldpassword==prepass.password:
                if oldpassword!=newpasssword:
                    if newpasssword==confirmpassword:
                        Login.objects.filter(userid=username).update(password=newpasssword)
                        return redirect('stundentlogout')
                    else:
                        messages.warning(request, "newpassword and confirm password not match")
                else:
                    messages.warning("password not be same as previous password")
            else:
                messages.warning(request,'password not match')
        return render(request,'changestupass.html',{"stu":stu})



@cache_control(no_cache=True,must_revalidate=True,no_store=True)        
def feedback(request):
    if request.session['username']!=None:
        username=request.session['username']
        stu=Registration.objects.get(username=username)
        if request.method=="POST":
            responcetype=request.POST['responcetype']
            subject=request.POST['subject']
            responcetext=request.POST['responcetext']
            responcedate=date.today()
            sr=StuResponce(username=stu.username,name=stu.name,branch=stu.branch,year=stu.year,email=stu.email,responcetype=responcetype,subject=subject,responcetext=responcetext,responcedate=responcedate)
            sr.save()
            messages.success(request,"responce submitted")
        return render(request,'feedback.html',{"stu":stu})
    

#def index(request):
 #   return render(request,'index.html')

