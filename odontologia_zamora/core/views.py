from email import message
import imp
from datetime import date, datetime
from time import strptime
from django.shortcuts import render, redirect
from django.urls import reverse
from contacto.forms import ContactoForm
from cita.forms import CitaForm
from cita.models import Cita
from doctor.models import doctor
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

# Create your views here.

def home(request):
    if request.method == "POST":
          form = ContactoForm(request.POST)
          form1 = CitaForm(request.POST)
          
    else:
          form = ContactoForm()
          form1 = CitaForm()

    context = {

          "form":form,
          "form1":form1,

     }
    return render(request, "core/index.html", context)

def contacto_form(request):
       if request.method == "POST":
          form = ContactoForm(request.POST)
          mail = request.POST.get('email')
          name = request.POST.get('name')
          procedure = request.POST.get('subject')
          if procedure == 'P':
              procedure = 'petición'
          elif procedure == 'Q':
              procedure = 'queja'
          elif procedure == 'R':
              procedure = 'reclamo'
          elif procedure == 'S':
            procedure = 'sugerencia'  
          form = ContactoForm(request.POST)
          if form.is_valid():
            form.save()
            return redirect(reverse('home')+'?ok-form')
          else:
            form = ContactoForm()
       return redirect('home')

def cita_form(request):
       
       if request.method == "POST":
          form = CitaForm(request.POST)
          if form.is_valid():
            today = datetime.today()
            date1 = request.POST.get("date")
            date2= datetime.strptime(date1, '%Y-%m-%dT%H:%M')
            doctor1 = request.POST.get("doctor")
            doctor1 = doctor.objects.get(id=doctor1)
            print(doctor1)
            print(Cita.objects.filter(doctor = doctor1))
            if date2 < today:
              return redirect(reverse('home')+'?date-wrong')
            elif Cita.objects.filter(doctor = doctor1 ):
              print("Estoy aqui")
            if Cita.objects.filter(date=date2):
              print("Ahora aqui")
              return redirect(reverse('home')+'?date-not-available')
            else:
              print("Nunca me fui")
              form.save()  
              return redirect(reverse('home')+'?ok-date')
          else:
            print(form.errors.as_data())
            form = CitaForm()
       return redirect('home')  

# def send_email(mail, name, procedure):
#     context = {'name': name, 'procedure': procedure}
#     template = get_template('core/email.html')
#     content = template.render(context)
#     email = EmailMultiAlternatives(
#         'Odontología Zamora',
#         'Soy Odontología Zamora',
#         settings.EMAIL_HOST_USER,
#         [mail]
#     )
#     email_self = EmailMultiAlternatives(
#         'Odontología Zamora',
#         'Soy Odontología Zamora',
#         settings.EMAIL_HOST_USER,
#         ["noreplyondontozamora@gmail.com"]
#     )
#     email.attach_alternative(content, 'text/html')
#     email.send()
#     email_self.attach_alternative(content, 'text/html')
#     email_self.send()