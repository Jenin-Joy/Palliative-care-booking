from django.urls import path,include
from User import views

app_name="User"
urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),#
    path('profile/',views.profile,name='profile'),#
    path('EditProfile/',views.editprofile,name='EditProfile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('addpatient/', views.addpatient, name='addpatient'),#
    path('sendrequest/<int:pid>/<int:plid>', views.sendrequest, name='sendrequest'),
    path('myrequest/', views.myrequest, name='myrequest'),#
    path('viewpaliativecare/<int:pid>', views.viewpaliativecare, name='viewpaliativecare'),
    path('complaint/',views.complaint,name='complaint'),#
    path("mybooking/",views.mybooking, name="mybooking"),#
    path("payment/<int:id>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'), 

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('logout/',views.logout,name="logout"),
]




