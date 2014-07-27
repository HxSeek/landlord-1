from django.contrib import admin

from landlord.student_activity_center.models import StudentActivityCenterApplication


class StudentActivityCenterApplicationAdmin(admin.ModelAdmin):
	list_display = ('organization', 'applicant_name')

admin.site.register(StudentActivityCenterApplication, StudentActivityCenterApplicationAdmin)

