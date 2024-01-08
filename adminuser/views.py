from django.shortcuts import render,redirect
from .models import Course,Student,Usermember
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    cs = Course.objects.all()
    return render(request,'signup.html',{'cs':cs})

def adminhome(request):
    return render(request,'adminhome.html')

def addcourse(request):
    if request.user.is_authenticated:
        return render(request,'course.html')
    else:
        return render(request,'home.html')


def addstudent(request):
    if request.user.is_authenticated:
        cs=Course.objects.all()
        return render(request,'student.html',{'cs':cs})
    else:
        return render(request,'home.html')
def courseadd(request):
    if request.method == 'POST':
        c = request.POST.get('course')
       
        f = request.POST.get('fee')
        crs=Course(Course_name=c,course_fee=f)
        crs.save()
        return redirect('addcourse')

    
def addteacher(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        email = request.POST['email']
        un = request.POST['username']
        pw = request.POST['password']
        cpw = request.POST['cpassword']
        adrs = request.POST['address']
        age = request.POST['age']
        contact = request.POST['contact']
        img = request.FILES.get('image')
        s = request.POST['sel']
        cr = Course.objects.get(id=s)

        if pw == cpw:
            if User.objects.filter(username=un).exists():
                messages.info(request,"Username already exists!!!")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=fn,
                    last_name=ln,
                    email=email,
                    username=un,
                    password=pw

                )
                user.save()
                um = Usermember(Adress=adrs,Age=age,Contact=contact,Image=img,course=cr,userr=user)
                um.save()
                return redirect('')
        else:
            messages.info(request,"Password doesn't match")
            return redirect('signup')
def logincheck(request):
    if request.method == 'POST':
        un = request.POST['uname']
        pw = request.POST['password']
        user = auth.authenticate(username=un,password=pw)
        if user is not None:
            if user.is_staff:
                login(request,user)
                messages.info(request,f'welcome admin')
                return redirect('adminhome')
            #request.session['uid']=user.id
            else:
                
                auth.login(request,user)
               
                messages.info(request,f'welcome {un}')
                return redirect('userhome')
        else:
            messages.info(request,"Invalid username or password...Try again!")
            return redirect('')
def userhome(request):
    user_id=request.user.id
    
    return render(request,'userhome.html',{'user_id':user_id})
def showteacher(request):
    
    customtr = Usermember.objects.all()

    return render(request,'showteacher.html',{'ctr':customtr})

def showstudent(request):
    if request.user.is_authenticated:
        st = Student.objects.all()
        return render(request,'showstudent.html',{'st':st})
    else:
        return render(request,'home.html')

    
def studentadd(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        adrs = request.POST['address']
       
        a = request.POST.get('age')
        date = request.POST['joining_date']
        s = request.POST['sel']
        cr = Course.objects.get(id=s)
        st = Student(Student_name=n,Student_address=adrs,Student_age=a,Joining_date=date,course=cr)
        st.save()
        return redirect('addstudent')
def editstudent(request,pk):
    st = Student.objects.get(id=pk)
    cs = Course.objects.all()
    return render(request,'editstudent.html',{'st':st,'cs':cs})
def update(request,pk):
    if request.method == 'POST':

        s = Student.objects.get(id=pk)
        s.Student_name=request.POST['name']
        s.Student_address=request.POST['address']
        s.Student_age=request.POST['age']
        s.Joining_date=request.POST['joining_date']
        sel = request.POST['sel']
        cs1 = Course.objects.get(id=sel)
        s.course = cs1
        s.save()
        return redirect('showstudent')
    return render(request,'editstudent.html')
def deletestud(request,pk):
    s = Student.objects.get(id=pk)
    s.delete()
    return redirect('showstudent')
def deleteteacher(request,pk):
    t = Usermember.objects.get(id=pk)
    t.delete()
    t.userr.delete()
    return redirect('showteacher')
def logout(request):
    auth.logout(request)
    return redirect('')



        

