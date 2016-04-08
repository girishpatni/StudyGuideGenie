from django.shortcuts import render
from django.utils import timezone
from .models import Notes

# Create your views here.

def Notes_list(request):
	notes = Notes.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request,'guide/Notes_list.html',{'notes':notes})

