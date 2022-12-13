from django.contrib import admin
from user.models import User


class UserAdmin(admin.ModelAdmin):
    read_only_fields = ('id', 'created_at', 'modified_at', 'password')


admin.site.register(User, UserAdmin)
