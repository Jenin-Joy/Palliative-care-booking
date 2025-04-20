from django.urls import path
from Panchayath import views
app_name="Panchayath"

urlpatterns = [
   path('homepage/',views.homepage,name="homepage"),
   path('viewuser/',views.viewuser,name="viewuser"),
   path('addward/',views.addward,name="addward"),
   path('delward/<int:id>/', views.delward, name='delward'),

   path('profile/',views.profile,name='profile'),#
   path('EditProfile/',views.editprofile,name='EditProfile'),
   path('changepassword/',views.changepassword,name='changepassword'),
   
   path('viewpaliativecare/',views.viewpaliativecare,name="viewpaliativecare"),
   path('verifypaliativecare/<int:id>/<int:status>',views.verifypaliativecare,name="verifypaliativecare"),

   path('logout/',views.logout,name="logout"),
   
]   