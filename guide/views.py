from django.shortcuts import render, render_to_response, RequestContext
from django.utils import timezone
from .models import Notes
from django.shortcuts import render, get_object_or_404
from .forms import signupform

# Create your views here.

def Notes_list(request):
	notes = Notes.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request,'guide/Notes_list.html',{'notes':notes})

def Notes_detail(request, pk):
	notes = get_object_or_404(Notes,pk=pk)
	return render(request,'guide/Notes_detail.html',{'notes':notes})

# def home(request):

def signup(request):
	form = signupform()
	return render(request,'guide/signup.html')

def login(request):
	# form = signupform()
	return render(request,'guide/login.html')
def home(request):
	return render(request,'guide/home.html')
def base2(request):
	return render(request,'guide/base2.html')
def signin(request):
	return render(request,'guide/signin.html')
def homepage(request):
	return render(request,'guide/homepage.html')
def index(request):
	return render(request,'guide/index.html')
# 
# def login(request):
# 	form =loginform
# 	return render_to_response("login.html",locals(),context_instance=RequestContext(request))
# 	
	


