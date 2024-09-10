# Business Logic 

from django.http import HttpResponse

from django.shortcuts import render

# from Templates import *


def signUp(request):
    print("****************************\n Studentis signdup successfully \n **************************************")
    
    # return HttpResponse("Successfully")
    return render(request, 'signup.html')