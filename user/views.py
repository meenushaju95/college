from django.shortcuts import render,redirect
from adminuser.models import Course
from adminuser.models import Usermember
from django.contrib.auth.models import User,auth

from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login

def editteacher(request,user_id):
    
    um = Usermember.objects.get(userr_id=user_id)
    cs = Course.objects.all()
    return render(request,'editteacher.html',{'um':um,'cs':cs}) 
def teacheredit(request, user_id):
    if request.method == 'POST':
        p = Usermember.objects.get(id=user_id)
        
        p.userr.first_name = request.POST['fname']
        p.userr.last_name = request.POST['lname']
        p.userr.username = request.POST['username']
        p.userr.email = request.POST['email']
        p.Adress = request.POST['address']
        p.Age = request.POST['age']
        p.Contact = request.POST['contact']

        if 'image' in request.FILES:
            p.Image = request.FILES['image']

        sel = request.POST['sel']
        cs1 = Course.objects.get(id=sel)
        p.course = cs1

        p.userr.save()
        p.save()

        return redirect('userhome')
def cardteacher(request,user_id):
    um = Usermember.objects.get(userr_id=user_id)
    return render(request,'cardteacher.html',{'um':um})

