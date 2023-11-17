from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
import vobject
from django.http import HttpResponse

from company.models import Company
from contact.models import Card
from tool.models import Utility
from user.models import User
from service.models import Service 

# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'home/home.html') 
    return redirect('home')

def company(request):
    if request.method == 'GET':
        
        return render(request, 'company/company.html')
    return redirect('home')

def card(request, slug):
    if request.method == 'GET':
        company = Company.objects.filter(is_active=True).first()
        contact = Card.objects.filter(is_active=True)
        tool = Utility.objects.filter(is_active=True)
        user = User.objects.prefetch_related('company', 'contact').filter(is_active=True, slug=slug).first()
        service = Service.objects.filter(is_active=True)
        ctx = {
            'company': company,
            'contact': contact,
            'tool': tool,
            'user': user,
            'service': service
        }
        return render(request, 'card/card.html', ctx) 
    return redirect('home')

def vcard(request, slug):
    user = get_object_or_404(User, slug=slug)
    vcard_data = vobject.vCard()
    vcard_data.add('n')
    vcard_data.n.value = vobject.vcard.Name(family=user.name, given='')
    vcard_data.add('fn')
    vcard_data.fn.value = user.name
    vcard_data.add('email')
    vcard_data.email.value = user.contact.mail
    vcard_data.email.type_param = 'Correo Electrónico'
    vcard_data.add('tel')
    vcard_data.tel.value = user.contact.mobile
    vcard_data.tel.type_param = 'Celular'
    vcard_data.add('tel')
    vcard_data.tel.value = user.contact.phone
    vcard_data.tel.type_param = 'Teléfono'
    vcard_data.add('url')
    vcard_data.url.value = user.contact.web
    vcard_data.url.type_param = 'Sitio Web'
    response = HttpResponse(vcard_data.serialize(), content_type='text/x-vCard')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format('{}.vcf'.format(user.name))
    return response





