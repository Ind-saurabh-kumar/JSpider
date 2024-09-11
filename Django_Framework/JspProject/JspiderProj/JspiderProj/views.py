

from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

def home(request):
    
    data=Product()
    
    data.name="Traditional Telephone"
    data.authorname=""
    data.newprice=5000
    data.oldprice=50000
    
    data.change=""
    
    data.discount=round(((data.oldprice-data.newprice)/data.oldprice)*100,2)
    
    if data.discount>=0:
        data.change="Discount by"
    else:
        data.change="Increase by"
        data.incr=round(((data.newprice-data.oldprice)/data.newprice)*100)
    return render(request, 'index.html', {'data':data})





def product(request):
    
    return render(request, 'product.html/')
