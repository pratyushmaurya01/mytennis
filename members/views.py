from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render

def members(request):
  mymembers = Member.objects.all().values()
  context = {
    'mymembers': mymembers,
  }
  return render(request,'all_members.html',context)

def details(request,id):
  mymembers = Member.objects.get(id = id)
  context = {
    'mymember': mymembers,
  }
  return render(request,'details.html',context)

def main(request):
  return render(request,'main.html')

def testing(request):
  context = {
    'fruits' : ['Apple' , 'Banana' ,'cherry']
  }
  return render(request,'template.html' , context)
