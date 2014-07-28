from django.contrib import admin

from landlord.common.models import Room
from landlord.stu_act.models import StuActCenterApply


class StuActCenterApplyAdmin(admin.ModelAdmin):
    list_display = ('organization', 'applicant_name')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(
    StuActCenterApply, StuActCenterApplyAdmin,
)

admin.site.register(
    Room, RoomAdmin,
)
