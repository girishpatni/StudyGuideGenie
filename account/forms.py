from django.contrib.auth.models import User
from django import forms
from account.models import SignUp,UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture')

class SignUpForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = SignUp
        fields ='__all__'

    
# class LoginForm(models.Model):
#     email = forms.EmailField(required = True)
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = ('email','password')
#         
#     def save(self,commit = True):   
#         user = super(RegistrationForm, self).save(commit = False)
#         user.email = self.cleaned_data['email']
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']       
#         if commit:
#             user.set_password(user.password)
#             user.save()
#             
#         return user