from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login
from .models import Course,Student,Teacher
import os
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

@login_required(login_url='homepage')
def adminhome(request):
    return render(request,'adminhome.html') 

@login_required(login_url='homepage')
def adminaddcourse(request):
    return render(request,'adminaddcourse.html')

@login_required(login_url='homepage')
def add_course(request):
    if request.method=='POST':
        cname=request.POST['course']
        fe=request.POST['fee']
        sp=Course(coursename=cname,fees=fe)
        sp.save()
        return redirect('adminaddstd')
    
@login_required(login_url='homepage')
def adminaddstd(request):
    cs=Course.objects.all()
    return render(request,'adminaddstd.html',{'crse':cs})

@login_required(login_url='homepage')
def addstd_details(request):
    if request.method=='POST':
        nam=request.POST['name']
        add=request.POST['address']
        ag=request.POST['age']
        dt=request.POST['date']
        dp=request.POST['c']
        cc=Course.objects.get(id=dp)
        std=Student(studentname=nam,address=add,age=ag,joiningdate=dt,course=cc)
        std.save()
        return redirect('adminshowstd')

@login_required(login_url='homepage')
def admineditstd(request,id):
    std=Student.objects.get(id=id)
    crcs=Course.objects.all()
    return render(request,'admineditstd.html',{'studt':std, 'cs':crcs})

@login_required(login_url='homepage')
def editstd_details(request,id):
    if request.method=='POST':
        ss=Student.objects.get(id=id)
        ss.studentname=request.POST['name']
        ss.address=request.POST['address']
        ss.age=request.POST['age']
        ss.joiningdate=request.POST['date']
        cor=request.POST['c']
        fee=request.POST['fee']
        course1=Course.objects.get(id=cor)
        course1.fees=fee
        course1.save()
        ss.course=course1
        ss.save()
        return redirect('adminshowstd')
    return render(request,'admineditstd.html')

@login_required(login_url='homepage')
def delete_std(request,id):
    stt=Student.objects.get(id=id)
    stt.delete()
    return redirect('adminshowstd')

@login_required(login_url='homepage')
def adminshowstd(request):
    std=Student.objects.all()
    return render(request,'adminshowstd.html',{'stud':std})

@login_required(login_url='homepage')
def adminshowteach(request):
    tchr=Teacher.objects.all()
    return render(request,'adminshowteach.html',{'tcr':tchr})

@login_required(login_url='homepage')
def delete_tchr(request,id):
    tt=Teacher.objects.get(id=id)
    tt.delete()
    return redirect('adminshowteach')


def teachsignpage(request):
    course=Course.objects.all()
    return render(request,'teachsignpage.html',{'crse':course})


def user_sign(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['uname']
        addr=request.POST['add']
        ag=request.POST['age']
        email=request.POST['mail']
        ph=request.POST['phone']
        password=request.POST['pass']
        cpassword=request.POST['cpass']
        im=request.FILES.get('img')
        cou=request.POST['c']
        
        
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists')
                return redirect('teachsignpage')
            else:
                user=User.objects.create_user(first_name=first_name,
                                              last_name=last_name,
                                              username=username,
                                              password=password,
                                              email=email)
                user.save()
                use=Course.objects.get(id=cou)
                u=User.objects.get(id=user.id)
                reg=Teacher(address=addr,age=ag,phone=ph,image=im,user=u,course=use)
                reg.save()
                return redirect('/')

        else:
            messages.info(request,'Password doesnot match')
            return redirect('teachsignpage')       
    else:
        return render(request,'homepage.html')    

@login_required(login_url='homepage')
def logout(request):
    auth.logout(request)
    return redirect('homepage')

def adminlog(request):
    if request.method=='POST':
        username=request.POST['usname']
        password=request.POST['passd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:   
                login(request,user)                
                return redirect('adminhome')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {user}')              
                return redirect('techhome')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('homepage')
    return render(request,'homepage.html')

@login_required(login_url='homepage')
def techhome(request):
    return render(request,'techhome.html')

@login_required(login_url='homepage')
def teachercard(request):
    tchr=Teacher.objects.get(user=request.user)
    cr=Course.objects.all()
    return render(request,'teachercard.html',{'tcr':tchr,'csr':cr})

@login_required(login_url='homepage')
def tchrcard(request,username):
    if request.method=='POST':
        t=Teacher.objects.get(id=username)
        user=User.objects.get(id=username)
        user.first_name=request.POST.get('fname')
        user.last_name=request.POST.get('lname')
        user.username=request.POST.get('uname')
        t.address=request.POST.get('add')
        t.age=request.POST.get('age')
        user.email=request.POST.get('mail')
        t.phone=request.POST.get('phone')
        t.image=request.POST.get('image')
    
    return render(request,'teachercard.html')

@login_required(login_url='homepage')
def back(request):
    return redirect('/')

@login_required(login_url='homepage')
def teachupdate(request):
    tch=Teacher.objects.get(user=request.user)
    crcs=Course.objects.all()
    return render(request,'teachupdate.html',{'tchr':tch, 'crse':crcs})

@login_required(login_url='homepage')
def tchr_edit(request,id):
    if request.method=='POST':
        t=Teacher.objects.get(user=id)
        user=User.objects.get(id=id)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.username=request.POST['uname']
        t.address=request.POST['add']
        t.age=request.POST['age']
        user.email=request.POST['mail']
        t.phone=request.POST['phone']
        courseid=request.POST['c']
        course=Course.objects.get(id=courseid)
        t.course=course
        t.image=request.FILES.get('img')
        
        t.save()
        user.save()
        return redirect('teachercard')



