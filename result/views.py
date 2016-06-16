from django.shortcuts import render
from django.http import HttpResponse
from result.models import Student
# Create your views here.

def index(request):
	return HttpResponse("this site works")

def by_total_marks(request,order = '1'):
	if order == '1':
		students = Student.objects.order_by('-total_marks')
	else:
		students = Student.objects.order_by('total_marks')

	return render(request,"result/by_total_marks.html",{'students':students,'order':order,'img':'saved_page/1318710049_files/635668695378952000.jpg'})

def by_internal_marks(request,order='1'):
	if order == '1':
		students = Student.objects.order_by('-total_internal')
	else:
		students = Student.objects.order_by('total_internal')
	return render(request,"result/by_internal_marks.html",{'students':students,'order':order})

def by_external_marks(request,order='1'):
	if order == '1':
		students = Student.objects.order_by('-total_external')
	else:
		students = Student.objects.order_by('total_external')
	return render(request,"result/by_external_marks.html",{'students':students,'order':order})


def profile(request,rno):
	return HttpResponse("querry for roll no %s"%rno)
