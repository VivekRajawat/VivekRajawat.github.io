from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('contact',views.contact,name='contact') 
]