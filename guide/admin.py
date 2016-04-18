from django.contrib import admin
from .models import Notes
# from account.models import UserProfile


class NotesAdmin(admin.ModelAdmin):
    class Meta():
        model= Notes
admin.site.register(Notes, NotesAdmin)
# admin.site.register(UserProfile)

        
    

