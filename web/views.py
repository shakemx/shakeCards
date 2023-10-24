from django.shortcuts import render, redirect
from datetime import datetime

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
            'service': service,
        }
        return render(request, 'card/card.html', ctx) 
    return redirect('home')

