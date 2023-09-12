from django.contrib import admin
from . models import User , Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.

    list_display = ["id" , "email", "name","designation", "is_admin" ,'is_active','is_staff', "created_at" , "updated_at"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name" , "designation"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name" , "designation", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email" , "name" , "designation"]
    ordering = ["email" , "id"]
    filter_horizontal = []

# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'profile_image']