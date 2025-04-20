from django.urls import path,include
from PaliativeCare import views

app_name="PaliativeCare"
urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('profile/',views.profile,name='profile'),
    path('EditProfile/',views.editprofile,name='EditProfile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('viewbooking/',views.viewbooking,name='viewbooking'),
    path('addamount/<int:id>',views.addamount,name='addamount'),
    path('rejectrequest/<int:id>',views.rejectrequest,name='rejectrequest'),

    path('logout/',views.logout,name="logout"),

    
]




