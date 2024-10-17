from django.contrib import admin
from .models import Emp,Testimonial

# Register your models here.
#customise data in admin from here
class EmpAdmin(admin.ModelAdmin):
    list_display=('emp_id','name','working','department','phone') #only display
    list_editable=('name',) #editable
    search_fields=('name','emp_id','department')
    list_filter=('working',)
    
admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)


