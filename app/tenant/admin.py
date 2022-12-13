from django.contrib import admin
from tenant.models import Tenant


class TenantAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tenant, TenantAdmin)
