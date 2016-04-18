from django.contrib import admin

# Register your models here.

from account.models import SignUp,UserProfile

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model= SignUp
admin.site.register(SignUp,SignUpAdmin)
admin.site.register(UserProfile)
