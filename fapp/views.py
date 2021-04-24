from django.shortcuts import render,redirect
from .models import addproject
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .form import mymodelform,myloginform
# Create your views here.
def addproject_form(request):
    return render(request,'addproject.html',{})

def addproject_database(request):
    obj=addproject()
    tittle= request.POST['tit']
    details = request.POST['det']
    cateogry = request.POST['cat']
    target = request.POST['target']
    img = request.POST['img']
    sdate = request.POST['sdate']
    enddate = request.POST['enddate']
    obj.tittle=tittle
    obj.details=details
    obj.category=cateogry
    obj.total_target=target
    obj.uploadimg=img
    obj.startdate=sdate
    obj.edndate=enddate
    obj.save()
    return redirect('homepage')

def addproject_table(request):
    obj2 = addproject.objects.all()
    return render(request, 'home.html', {'data': obj2})


#def register_form(request):
 #   return render(request,'adduser.html',{})
def register(request):
    if request.method=='POST':
        form=mymodelform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user=User.objects.create_user(username=uname,email=email,password=password)
            user.save()
            return HttpResponse('user added')
    else:
        form=mymodelform()
    return render(request,'adduser.html',{'form':form})
# def login_form(request):
#    return render(request,'login.html',{})
def log_user(request):
    if request.method == 'POST':
        form = myloginform(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=authenticate(username=uname, password=passsword)
            # user=User.objects.filter(username=uname,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse('user added')
            else:
                return HttpResponse("not found")
    else:
        form = myloginform()
    return render(request, 'login.html', {'form': form})

    #     if request.method=='POST':
    #     form=myModelForm(request.POST)
    #     if form.is_valid():
    #         fname=form.cleaned_data['first_name']
    #         pas=form.cleaned_data['password']
    #         user=authenticate(username=fname, password=pas)
    #         if user is not None:
    #             login(request)
    #             return HttpResponse("user login")
    #         else:
    #             return HttpResponse("not found")
    # else:
    #     form = myModelForm()
    # return render(request, 'loginAuth.html', {'form':form})