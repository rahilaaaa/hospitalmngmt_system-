from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('about/',views.About,name='about'),
    path('booking/',views.Booking,name='booking'),
    path('doctors/',views.Doctors,name='doctors'),
    path('contact/',views.Contact,name='contact'),
    path('department/',views.Department,name='department'),
    path('login/',views.Login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.Logout,name='logout'),







]