from django.conf import settings
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail


# Create your views here.


def contact(request):
    my_info = Info.objects.first()
    context = {'info': my_info}
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        send_mail(
            f'Job-Board Contact for subject: {subject}',
            f'from: {name}\nemail: {email}\nmessage:\n\t{message}',
            settings.EMAIL_HOST_USER,
            ['mahmoudfathiibrahim@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html', context)
