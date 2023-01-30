from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.log_fun,name='log'),#it will display login function
    path('reg',views.reg_fun,name='reg'),  #it will redirect to register.htmlpage
    path('regdata',views.regdata_fun),#it will create super user account
    path('logdata',views.log_read),
    path('home',views.home_fun,name='home'),
    path('add_students',views.addstudent_fun,name='add'),
    path('readdata',views.readdata_fun),#it will insert records in to studenttable
    path('display',views.display_fun,name='display'),#it will display student table data in display.html
    path('update/<int:id>',views.update_fun,name='up'),#it will update the student record
    path('delete/<int:id>',views.delete_fun,name='del'),#it will delete the student
    path('log_out',views.log_out_fun,name='log_out')
]


