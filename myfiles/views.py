from django.shortcuts import render
from myfiles.models import *
import datetime
# Create your views here.
def index(malumot):
    ishlarimiz = Portfolio.objects.all()
    ishchilar = Team.objects.all()
    hodim = Services.objects.all()
    saqlash = Malumot_saqlash.objects.all()
    if 'he' in malumot.POST:
        emaili = malumot.POST.get('he')
        Ali(email=emaili,date=datetime.datetime.now()).save()

    elif 'idd' in malumot.POST:
        emaili = malumot.POST.get('idd')
        Subject(email=emaili,date=datetime.datetime.now()).save()
    elif malumot.method == "POST":
        ismi = malumot.POST.get('name')
        email = malumot.POST.get('email')
        mavzusi = malumot.POST.get('subject')
        xabari = malumot.POST.get('message')
        Malumot_saqlash(name=ismi, email=email, subject=mavzusi, message=xabari,date=datetime.datetime.now()).save()
    return render(malumot,'index.html',{"works":ishlarimiz,"jamoa":ishchilar,"servis":hodim,"saqlash":saqlash})

def malumot_qoshish(malumot):
    return render(malumot,'index.html')

def subject(malumot):
    return render(malumot,'index.hhtml')







def portfolio(malumot,id):
    ishlarimiz = Portfolio.objects.get(id=id)
    return render(malumot , 'portfolio-details.html',{"work":ishlarimiz})




















