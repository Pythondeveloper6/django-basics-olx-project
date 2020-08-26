from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.



def sendemail(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        send_mail(
        f'from {email} - subject {subject}',
        f'message from {email} : message {message}',
        email,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )


    return render(request,'contact/contact.html',{})