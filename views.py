from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def product_details(request):
    return render(request, 'product-details.html')
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        # Here, handle form data or send an email
        # name = request.POST.get('name') etc.
        return render(request, 'contact.html', {'success_message': 'Thank you! Your message has been sent.'})
    return render(request, 'contact.html')
