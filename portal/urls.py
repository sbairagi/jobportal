from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('logout', views.Logout, name="logout"),
    path('userhome', views.Userhome, name="userhome"),
    path('companyhome', views.Companyhome, name="companyhome"), 
    path('viewmyjobs', views.Viewmyjobs, name="viewmyjobs"),  
    path('viewallapplicant/<int:id>', views.Viewallapplicant, name="viewallapplicant"), 
    path('applyjob/<int:id>', views.Applyjob, name="applyjob"),
    path('sucessfullyApply/<int:id>', views.SucessfullyApply, name="sucessfullyApply"),
    path('sucessfullyshortlistcandident/<int:id>', views.Sucessfullyshortlistcandident, name="Sucessfullyshortlistcandident"),
    
]
