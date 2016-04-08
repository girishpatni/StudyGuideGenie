from django.shortcuts import render

# Create your views here.

def Notes_list(request):
	return render(request,'guide/Notes_list.html',{})

