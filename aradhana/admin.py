from django.contrib import admin
from .models import Student,Event
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list_display=('name','school','standard')
	list_filter=('standard','school')
	search_fields=('name',)
	filter_horizontal=('events',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Event)