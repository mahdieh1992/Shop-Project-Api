from django.contrib import admin
from .models import CustomUser,UserProfile
from django.contrib.auth.admin import UserAdmin




class CustomUserAdmin(UserAdmin):
    """
        filter.ordering,search and grouping fields
    """
    model=CustomUser
    list_display=('email','is_staff',)
    list_filter=('date_join','is_active',)
    ordering = ("email",)
    fieldsets=(
        ('info',{'fields':('email',)}),
        ('Permission',{'fields':('is_staff','is_active',)})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active"
            )}
        ),
    )

admin.site.register(UserProfile)
admin.site.register(CustomUser,CustomUserAdmin)
# Register your models here.
