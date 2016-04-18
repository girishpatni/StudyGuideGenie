from django.shortcuts import render_to_response,render,RequestContext
from django.http import HttpResponseRedirect    
from django.contrib import auth                 
from django.template.context_processors import csrf
from account.forms import SignUpForm,UserForm,UserProfileForm
from django.contrib import messages

def landing_view(request):
    context=RequestContext(request)
    return render(request,'guide/index.html',context)

def home_view(request):
    context = RequestContext(request)
    return render_to_response('guide/home.html', {}, context)


def login_view(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect('guide/index.html')
            else:
                return HttpResponse("Account is Disabled")
        else:
            return HttpResponse("Invalid login credentials .")
    else:
        return HttpResponseRedirect('guide/home.html')
 
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('guide/home.html')

def register_view(request):
    context = RequestContext(request);
    registered = False
    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']
            profile.save()
            messages.success(request,'Successfully Registered')
            registered=True
            return HttpResponseRedirect('/guide/index.html')
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render_to_response('guide/home.html',{'user_form': user_form, 'profile_form': profile_form,'registered': registered},context)       

