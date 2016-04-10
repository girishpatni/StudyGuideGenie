from django.shortcuts import render
from django.utils import timezone
from .models import Notes
from django.shortcuts import render, get_object_or_404


# Create your views here.

def Notes_list(request):
	notes = Notes.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request,'guide/Notes_list.html',{'notes':notes})

def Notes_detail(request, pk):
	notes = get_object_or_404(Notes,pk=pk)
	return render(request,'guide/Notes_detail.html',{'notes':notes})


