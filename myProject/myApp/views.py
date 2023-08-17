from django.shortcuts import render
from .models import myData
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# Create your views here.
def index(request):
  data = myData.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'alldata': data,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  templetes=loader.get_template('add.html')
  return HttpResponse(templetes.render({},request))

def addrecord(request):
  name=request.POST['name']
  age=request.POST['age']
  email=request.POST['email']
  phone=request.POST['phone']
  alldata=myData(Name=name,Age=age,Email=email,Phone=phone)
  alldata.save()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  data = myData.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'alldata': data,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  name = request.POST['name']
  age = request.POST['age']
  email = request.POST['email']
  phone = request.POST['phone']
  member = myData.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))



