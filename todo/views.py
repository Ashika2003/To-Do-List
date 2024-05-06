from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import Todoform
from .models import TodoModel
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'todo/index.html')

def login_user(request):
    if request.method=='POST':
        forms=AuthenticationForm(data=request.POST)
        if forms.is_valid():
            username=forms.cleaned_data['username']
            password=forms.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/todo/')
        return HttpResponseRedirect('/login/')
        
    forms=AuthenticationForm()
    return render(request,'todo/login.html',{'forms':forms})
    

def signup(request):
    if request.method=='POST':
        forms=UserCreationForm(request.POST)
        if forms.is_valid:
            forms.save()
            return HttpResponseRedirect('/login/')

        
    
    forms=UserCreationForm()
    return render(request,'todo/signup.html',{'forms':forms})
    
def todo(request):
    if request.method=='POST':
        forms=Todoform(request.POST)
        if forms.is_valid():
            title=forms.cleaned_data['title']
            status=forms.cleaned_data['status']
            due_date=forms.cleaned_data['due_date']
            user=forms.cleaned_data['user']
            priority=forms.cleaned_data['priority']
            task=TodoModel(title=title,status=status,due_date=due_date,user=user,priority=priority)
            task.save()
            return  HttpResponseRedirect('/tasks/')
        forms=Todoform()
    forms=Todoform
    return render(request,'todo/todo.html',{'forms':forms})

def task(request):
    tasks=TodoModel.objects.all()
    return render(request,'todo/tasks.html',{'tasks':tasks})

def deletetask(request,id):
    pk=id
    task=TodoModel.objects.get(pk=id)
    task.delete()
    return HttpResponseRedirect('/tasks/')

def updatetask(request,id):
    if request.method=='POST':
         pi=TodoModel.objects.get(pk=id)
         fm=Todoform(request.POST,instance=pi)
         if fm.is_valid:
             fm.save()
             return HttpResponseRedirect('/tasks/')
    else:
         pi=TodoModel.objects.get(pk=id)
         fm=Todoform(instance=pi)
    return render(request,'todo/update.html',{'forms':fm})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')
