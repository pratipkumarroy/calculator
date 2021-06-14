from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test1_view(request):
	return render(request,"home.html")

def addition(request):
	n1=int(request.GET["num1"])
	n2=int(request.GET["num2"])
	add=n1+n2
	return render(request,"add.html",{"addition":add})

def substraction(request):
	n1=int(request.GET["num1"])
	n2=int(request.GET["num2"])
	sub=n1-n2
	return render(request,"sub.html",{"substraction":sub})

def multiplication(request):
	n1=int(request.GET["num1"])
	n2=int(request.GET["num2"])
	mul=n1*n2
	return render(request,"mul.html",{"multiplication":mul})

def division(request):
	n1=int(request.GET["num1"])
	n2=int(request.GET["num2"])
	div=n1/n2
	return render(request,"div.html",{"division":div})
