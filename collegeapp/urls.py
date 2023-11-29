from django.urls import path
from .import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('adminlog',views.adminlog,name='adminlog'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('adminaddcourse',views.adminaddcourse,name='adminaddcourse'),
    path('add_course',views.add_course,name='add_course'),
    path('adminaddstd',views.adminaddstd,name='adminaddstd'),
    path('addstd_details',views.addstd_details,name='addstd_details'),
    path('admineditstd/<int:id>',views.admineditstd,name='admineditstd'),
    path('editstd_details/<int:id>',views.editstd_details,name='editstd_details'),
    path('delete_std/<int:id>',views.delete_std,name='delete_std'),
    path('adminshowstd',views.adminshowstd,name='adminshowstd'),
    path('adminshowteach',views.adminshowteach,name='adminshowteach'),
    path('delete_tchr/<int:id>',views.delete_tchr,name='delete_tchr'),
    path('techhome',views.techhome,name='techhome'),
    path('teachsignpage',views.teachsignpage,name='teachsignpage'),
    path('user_sign',views.user_sign,name='user_sign'),
    path('logout',views.logout,name='logout'),
    path('teachercard',views.teachercard,name='teachercard'),
    path('tchrcard/<str:username>',views.tchrcard,name='tchrcard'),
    path('back',views.back,name='back'),
    path('teachupdate',views.teachupdate,name='teachupdate'),
    path('tchr_edit/<int:id>',views.tchr_edit,name='tchr_edit'),

    
    

    
   
]