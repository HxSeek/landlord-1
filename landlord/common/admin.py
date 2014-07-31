from django.contrib import admin

from landlord.common.models import Room
from landlord.stu_act.models import StuActCenterApp
from landlord.mroom.models import MroomApp


class StuActCenterAppAdmin(admin.ModelAdmin):
    list_display = ('organization', 'applicant_name')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MroomAppAdmin(admin.ModelAdmin):
    list_display = ('organization', 'meeting_topic')


admin.site.register(
    StuActCenterApp, StuActCenterAppAdmin,
)

admin.site.register(
    Room, RoomAdmin,
)

admin.site.register(
    MroomApp, MroomAppAdmin,
)
