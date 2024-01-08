from .import views
from django.urls import path


urlpatterns = [
    path('',views.home,name=''),
    path('signup',views.signup,name='signup'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('courseadd',views.courseadd,name='courseadd'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('addteacher',views.addteacher,name='addteacher'),
    path('deleteteacher/<int:pk>',views.deleteteacher,name='deleteteacher'),
    path('logincheck',views.logincheck,name='logincheck'),
    path('userhome',views.userhome,name='userhome'),
    path('showteacher',views.showteacher,name='showteacher'),
    
    
    
    path('showstudent',views.showstudent,name='showstudent'),
     path('studentadd',views.studentadd,name='studentadd'),
     path('editstudent/<int:pk>',views.editstudent,name='editstudent'),
     path('update/<int:pk>',views.update,name='update'),
     path('deletestud<int:pk>',views.deletestud,name='deletestud'),
     path('logout',views.logout,name='logout')
    
]