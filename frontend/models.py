from django.db import models
from Accounts.models import Department

VISIBILITY_CHOICES = [
    ('public', 'Public (No Login Required)'),
    ('authenticated', 'Login Required'),
    ('department', 'Department Based'),
]

class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    departments = models.ManyToManyField(Department, blank=True)
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')

    def __str__(self):
        return self.name


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="submenus")
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    departments = models.ManyToManyField(Department, blank=True)
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')  # ✅ Added

    def __str__(self):
        return f"{self.menu.name} → {self.name}"


class ChildMenu(models.Model):
    submenu = models.ForeignKey(SubMenu, on_delete=models.CASCADE, related_name="child_menus")
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    departments = models.ManyToManyField(Department, blank=True)
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')  # ✅ Added

    def __str__(self):
        return f"{self.submenu.menu.name} → {self.submenu.name} → {self.name}"
