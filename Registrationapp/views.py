from django.shortcuts import render,HttpResponse,redirect
from .models import Contact

# Create your views here.
def index(request):
    if request.method=='POST':
        name =request.POST.get('name','')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        skills = request.POST.get('skills', '')
        phone = request.POST.get('phone', '')
        if name and email and password and skills and phone:
            contact=Contact(name=name,email=email,password=password,skills=skills,phone=phone)
            contact.save()
        else:
            return HttpResponse('enter all the details')
    return render(request, 'index.html')
