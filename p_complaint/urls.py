"""
URL configuration for p_complaint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from a_complaint import views

urlpatterns = [  
    path('',views.SignIN,name='logout'),
    path('homepage/',views.HomePage,name='homepage'),
    path('admin/', admin.site.urls),
    path('complaints/',views.CompList,name='complaints_list'),
    path('add/',views.CompAdd,name='add_complaint'),
    path('delete/<int:id>',views.DeleteComp,name='delete_complaint'),
    path('edit/<int:id>',views.CompUpdate,name='update_complaint'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('register/',views.Registration,name='register')

]
 

