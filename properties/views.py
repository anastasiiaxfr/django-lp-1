from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Property
from properties.choises import property_type, price_choices

# Create your views here.
def index(request):
    properties = Property.objects.order_by('-rent_date').filter(is_published=True)
    
    paginator = Paginator(properties, 6)
    page = request.GET.get('page') 
    paged_properties = paginator.get_page(page) 
    
    # Calculate page range for pagination (show 4 pages around current)
    current_page = paged_properties.number
    total_pages = paged_properties.paginator.num_pages
    start_page = max(1, current_page - 1)
    end_page = min(total_pages, current_page + 2)
    page_range = list(range(start_page, end_page + 1))
    
    context = {
        'properties': paged_properties,
        'page_range': page_range,
        'property_type': property_type,
        'price_choices': price_choices,
        'values': request.GET
    }
    
    return render(request, 'pages/properties/properties.html', context)

def property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    context = {
        'property': property
    }
    return render(request, 'pages/properties/property.html', context)

def search(request):
    queryset_list = Property.objects.order_by('-rent_date') 
    
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
            
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__icontains=city)

    if 'property_type' in request.GET:
        property_type_filter = request.GET['property_type']
        if property_type_filter and property_type_filter != 'All Types':
            queryset_list = queryset_list.filter(property_type__icontains=property_type_filter)

    # if 'price' in request.GET:
    #     price = request.GET['price']
    #     if price:
    #         try:
    #             queryset_list = queryset_list.filter(price__lte=int(price))
    #         except ValueError:
    #             pass

    context = {
        'property_type': property_type,
        'price_choices': price_choices,
        'properties': queryset_list,
        'values': request.GET
    }
    return render(request, 'pages/properties/search.html', context)  