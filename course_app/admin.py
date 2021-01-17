from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from .models import User, Mentor, Student, Event, Project, University, Faculty, Department
# Register your models here.

class UserResource(resources.ModelResource):
    
    class Meta:
        model=User
        
class UserIE(ImportExportActionModelAdmin):
    resource_class = UserResource
    list_display = ('first_name', 'second_name', 'stud_or_stuff', 'faculty_id', 'university_id')
    list_filter = ('stud_or_stuff', 'faculty_id', 'first_name')
        
admin.site.register(User, UserIE)
admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(Event)
admin.site.register(Project)
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Department)
