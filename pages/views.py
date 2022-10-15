from django.shortcuts import render, redirect
from cars.models import Car
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .tasks import send_mail_task

def home(request):
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)


def services(request):
    return render(request, 'pages/services.html')
  

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message_q = request.POST['message']

        email_subject = 'You have a new message from CarNepal website regarding ' + subject
        message = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message_q
        send_mail_task.delay(email_subject, message)

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email
        # send_mail(subject = email_subject,message = message,from_email = settings.EMAIL.HOST.USER,receipient = [admin_email],fail_silently=False,)

        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')
