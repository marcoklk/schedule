from django.contrib import admin
from .models import *

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass

@admin.register(PartTime)
class PartTimeAdmin(admin.ModelAdmin):
    pass

@admin.register(BaseTime)
class BaseTimeAdmin(admin.ModelAdmin):
    pass

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(Shift)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(YearSchedule)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(Schedule)
class UnitAdmin(admin.ModelAdmin):
    pass