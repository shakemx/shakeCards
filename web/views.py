from django.shortcuts import render, redirect, get_object_or_404
from os import environ
import vobject
from django.http import HttpResponse

from company.models import Company
from user.models import User

# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'home/home.html') 
    return redirect('home')

def company(request, slug):
    if request.method == 'GET':
        company = get_object_or_404(Company, slug=slug)
        users = User.objects.prefetch_related('tool').filter(company=company, is_active=True)
        ctx = {
            'company': company,
            'users': users,
        }
        return render(request, 'company/company.html',context=ctx)
    return redirect('home')

def card(request, slug):
    if request.method == 'GET':
        user = User.objects.prefetch_related('tool').filter(slug=slug,is_active=True).first()
        if user:
            company = Company.objects.prefetch_related('user').first()
            tool = user.tool.prefetch_related('icon').filter(is_active=True)
            tool_company = company.tool.prefetch_related('icon').filter(is_active=True)
            qr_user = '{}{}/{}'.format('https://', 'sensum.mx/agente', user.slug)
            ctx = {
                'user': user,
                'company': company,
                'tool': tool,
                'tool_company': tool_company,
                'qr_user': qr_user,
            }
            return render(request, 'card/card.html', context=ctx) 
        else:
            return redirect('home')
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





