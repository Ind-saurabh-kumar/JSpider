

from django.shortcuts import render, redirect
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




# product page *********************************************************************************
def product(request):
    
    return render(request, 'product.html/')


# welcome page *********************************************************************************
def welcomePage(request):
    
    return render(request, 'welcome.html', {'subject':'Python'})

# Employee page logic **************************************************************************
def empPage(request):
    if request.method == 'GET':
        return render(request, 'emp.html')

    if request.method == 'POST':
        eid = request.POST.get('eid')
        ename = request.POST.get('ename')
        esal = request.POST.get('esal')

        if not eid or not ename or not esal:
            return redirect('fail')
        else:
            return redirect('success')
 
def success(request):
    return render(request, 'success.html')

def fail(request):
    return render(request, 'fail.html')