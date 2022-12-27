from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def naga(request):
    fo=FormName()
    d={'fo':fo}
    if request.method=='POST':
        formname=FormName(request.POST)
        if formname.is_valid():
            n=formname.cleaned_data['name']
            a=formname.cleaned_data['age']
            e=formname.cleaned_data['email']
            g=formname.cleaned_data['gender']
            c=formname.cleaned_data['cources']
            d1={'n':n,'a':a,'e':e,'g':g,'c':c}
            return render(request,'brock.html',d1)
    
    return render(request,'naga.html',d)