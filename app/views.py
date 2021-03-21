from django.shortcuts import render
from . import forms
from subscribe.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.
def subscribe(request):
    sub = forms.subscribe()
    if request.method =='POST':
        sub = forms.subscribe(request.POST)
        subject = "Welcome!!"
        message = "Hey buddy, Thanks for joining our Community"
        recepient = str(sub['Email'].value())     


        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request,'success.html',{'recepient':recepient})
    
    return render(request,'index.html',{'form':sub})

