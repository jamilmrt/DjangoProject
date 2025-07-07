from django.shortcuts import render
from django.http import HttpResponse
from .models import Product  # Assuming you have a Product model defined in models.py


# Create your views here.

def index(request):
    products = Product.objects.all()  # Fetch all products from the database
    noOfSlides = len(products) // 4 + (len(products) % 4 > 0)  # Calculate number of slides
    
    params = {
        'noOfSlides': noOfSlides,
        'range': range(1, noOfSlides + 1),
        'products': products
    }
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    return render(request, 'shop/contact.html')
def tracker(request):
    return render(request, 'shop/tracker.html')
def search(request):
    return render(request, 'shop/search.html')
def productView(request, myid):
    # Fetch the product using myid
    # product = get_object_or_404(Product, id=myid)
    return render(request, 'shop/productView.html', {'myid': myid}) 
def checkout(request):
    return render(request, 'shop/checkout.html')    
# Note: The productView function currently does not fetch a product from the database.