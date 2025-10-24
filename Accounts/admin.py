from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, Department, Designation

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Users)
class UsersAdmin(UserAdmin):
    model = Users
    list_display = ['username', 'email', 'employee_id', 'department', 'designation', 'is_active', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'gender', 'department', 'designation']
    search_fields = ['username', 'email', 'employee_id']
    ordering = ['username']

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': (
                'employee_id', 'department', 'designation',
                'gender', 'birthdate', 'marital_status',
                'blood_grp', 'phone', 'address',
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'classes': ('wide',),
            'fields': (
                'employee_id', 'department', 'designation',
                'gender', 'birthdate', 'marital_status',
                'blood_grp', 'phone', 'address',
            ),
        }),
    )
