from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('contact/', views.contact, name='contact'),
    path("about/",views.about,name='about'),
    path("profile/",views.profile,name="profile"),
    path('profile/password/', views.change_password, name='change_password'),
    path('signout/', views.signout, name='signout'),
    
]