from django.shortcuts import render,redirect
from .models import Comp
from .forms import CompForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

#This view redirects to homepage
def HomePage(request):
    return render(request,'homepage.html')

#This view displays the list of complaints for the logged-in user
def CompList(request):
    complaint=Comp.objects.filter(user=request.user)
    return render(request,'complaints.html',{'complaint':complaint})
    
#This view allows adding a new complaint
@login_required(login_url="login")
def CompAdd(request):
    form=CompForm()
    if request.method=='POST':
        form=CompForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.user = request.user
            comp.save()
            return redirect('complaints_list')
    return render(request,'addcomplaint.html',{'form':form})

#This view allows updating an existing complaint
@login_required(login_url="login")
def CompUpdate(request,id):
    complaint=Comp.objects.get(id=id)
    form=CompForm(instance=complaint)
    if request.method=='POST':
        form=CompForm(request.POST,instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('complaints_list')
    return render(request,'addcomplaint.html',{'form':form})

#This view allows deleting a complaint
@login_required(login_url="login")
def DeleteComp(request,id):
    complaint=Comp.objects.get(id=id)
    complaint.delete()
    return redirect('complaints_list')

#This view handles the user registration
def Registration(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html',{'form':form})

#This view handles user login
def LoginPage(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('homepage')
    return render(request,'login.html',{'form':form})

#This view handles user logout
@login_required(login_url="login")
def Logout(request):
    logout(request)
    return render(request,'logout.html')

#This view redirects to logout page
def SignIN(request):
    return render(request,'logout.html')