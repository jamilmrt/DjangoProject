from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    return render(request, 'blog/index.html')

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