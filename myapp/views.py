from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from . models import Contact
# from django.contrib.auth.forms import AuthenticationForm
from . forms import RegisterForm, LoginForm

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse('<h1>My First Django Application</h1>')

def about(request):
    return render(request, 'about.html')

# def contact(request):
#     # if request.GET:
#     #     fullname=request.GET.get('fullname')
#     #     email_id=request.GET.get('email_id')
#     #     message=request.GET.get('message')
#     #     context={"fullname":fullname, "email_id":email_id, "message":message}
#     #     return render(request, 'contact.html', context)
#     if request.POST:
#             fullname=request.POST.get('fullname')
#             email_id=request.POST.get('email_id')
#             message=request.POST.get('message')
#             context={"fullname":fullname, "email_id":email_id, "message":message}
#             return render(request, 'contact.html', context)
#     else:
#         return render(request, 'contact.html')

def contact(request):
    if request.method=='POST':
        cont=Contact()
        cont.fullname=request.POST.get('fullname')
        cont.email_id=request.POST.get('email_id')
        cont.message=request.POST.get('message')
        try:
            cont.save()
            messages.success(request, 'Message save successfully')
        except Exception as e:
            messages.error(request, 'Message not save successfully')
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')

def viewContact(request):
    if request.user.is_authenticated:
        contacts=Contact.objects.all()
        context={'contacts':contacts}
        return render(request, 'viewcontact.html', context)
    else:
        return redirect('login-page')  

def delContact(request, id):
    try:
        contact=Contact.objects.get(id=id)
        contact.delete()
        messages.success(request, 'Contact details remove successfully')
    except Exception as e:
        messages.error(request, 'Contact details not remove successfully')
    return redirect('cont-view-page')

def updateContact(request, id):
    contact=get_object_or_404(Contact, id=id)
    if request.POST:
        try:
            contact.fullname=request.POST.get('fullname')
            contact.email_id=request.POST.get('email_id')
            contact.message=request.POST.get('message')
            contact.save()
            messages.success(request, 'Successfully update contact details')
        except Exception as e:
            messages.error(request, 'Successfully not update contact details')
        return redirect('cont-view-page')
    return render(request, 'updatecontact.html', {"contact":contact})

# User Registration
def register(request):
    if request.POST:
        form=RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your registration is successfully done')
            except Exception as e:
                messages.error(request, 'Your registration is unsuccessfull')
    form=RegisterForm()
    return render(request, 'registration.html', {'form':form})

def userLogin(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cont-view-page')
        else:
            messages.error(request, 'Invalid username or password')
            form=LoginForm()
    else:
        form=LoginForm()
    return render(request, 'userlogin.html', {'form':form})

def userLogout(requst):
    logout(requst)
    return redirect('login-page')