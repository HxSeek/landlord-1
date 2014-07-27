from django.contrib import admin

from landlord.account.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('user', 'chinese_name', 'org_in_charge', 'belong_to')

admin.site.register(Organization, OrganizationAdmin)
