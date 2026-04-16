from django.shortcuts import render

from properties.models import Property

def index(request):
    properties = Property.objects.order_by('-rent_date').filter(is_published=True)[:3]
    context = {
        'properties': properties
    }
    
    return render(request, 'pages/index.html', context)

def contact(request):
    return render(request, 'pages/contact.html')

