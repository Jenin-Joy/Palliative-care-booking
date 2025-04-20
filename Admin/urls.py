from django.contrib import admin
from django.urls import path,include
from Admin import views

app_name="Admin"

urlpatterns = [
    path('add/',views.add,name='add'),
    path('Largest/',views.largest,name='largest'),
    path('Calculator/',views.calculator,name='calculator'),


    path('homepage/',views.homepage,name='homepage'),

    path('District/',views.district,name='district'),
    path('deldistrict/<int:id>',views.deldistrict,name='deldistrict'),
    path('eddistrict/<int:id>',views.eddistrict,name='eddistrict'),

    path('Category/',views.category,name='Category'),
    path('AdminReg/',views.adminreg,name='Adminreg'),
    path('deladmin/<int:id>',views.deladmin,name='deladmin'),

    path('place/',views.place,name='place'),
    path('delplace/<int:id>',views.delplace,name='delplace'),
    path('editplace/<int:id>',views.editplace,name='editplace'),

    path('Viewpanchayath/',views.Viewpanchayath,name="Viewpanchayath"),
    path('viewpanchayathaccept/<int:id>',views.viewpanchayathaccept,name="viewpanchayathaccept"),
    path('viewpanchayathreject/<int:id>',views.viewpanchayathreject,name="viewpanchayathreject"),

    path('Ward/',views.ward,name='ward'),
    path('delward/<int:id>/', views.delward, name='delward'),
    
    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('replyedcomplaint/',views.replyedcomplaint,name="replyedcomplaint"),
    path('replycomplaint/<int:id>',views.replycomplaint,name="replycomplaint"),

    path('logout/',views.logout,name="logout"),
]