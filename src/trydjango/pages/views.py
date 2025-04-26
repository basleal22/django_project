from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):# *args,keyword args
    #return HttpResponse("<h1>hello world</h1>")#string of html code
    return render(request,"home.html",{})
def contact_view(request,*args,**kwargs):
    #return HttpResponse("<h1>contact_page</h1>")
    return render(request, 'contact.html',{})
def about_view(request,*args,**kwargs):
    my_context =  {"my_text":"this is about me",
                   "my_number": 925545444,
                   "list_items":[133,3534,775]}
    
    return render(request, 'about.html',my_context)
