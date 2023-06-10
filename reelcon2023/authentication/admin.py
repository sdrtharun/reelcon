from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Customize the fields displayed in the admin list view
    list_display = ('username', 'email', 'instagram_username','instagram_profile_link','phone_number', 'is_staff', 'is_active')

    # Customize the fields displayed in the admin detail/edit view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'instagram_username','instagram_profile_link','phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
