from django.contrib import admin

from landlord.stu_act.models import StuActCenterApp


class StuActCenterAppAdmin(admin.ModelAdmin):
    list_display = ('organization', 'applicant_name')


admin.site.register(
    StuActCenterApp,
    StuActCenterAppAdmin,
)
