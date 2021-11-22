from django.contrib import admin
from .models import CreateJob, ApplyUser

# Register your models here.


@admin.register(CreateJob)
class CreateJonAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'job_desc', 'experience', 'open_position')

admin.site.register(ApplyUser)