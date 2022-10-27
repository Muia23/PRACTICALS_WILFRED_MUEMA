from django.contrib import admin
from .models import(
    Stream,
    Student
)
# Register your models here.

class StreamAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Stream,StreamAdmin)

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Student,StudentAdmin)