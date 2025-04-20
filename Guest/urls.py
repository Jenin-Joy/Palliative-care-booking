
from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns = [
    path('login/',views.login,name='login'),
    path('Registration/',views.registration,name='Registration'),
    path('Ajaxplace/',views.Ajaxplace,name='Ajaxplace'),
    path('ajaxpanchayath/',views.ajaxpanchayath,name='ajaxpanchayath'),
    path('ajaxward/',views.ajaxward,name='ajaxward'),
    path('Panchayath/',views.Panchayath,name='Panchayath'),
    path('',views.index,name='index'),
    path('Addpaliativecare/',views.Addpaliativecare,name="Addpaliativecare"),
]