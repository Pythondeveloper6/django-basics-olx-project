from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.



def sendemail(request):
    send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)


    return render(request,'contact/contact.html',{})