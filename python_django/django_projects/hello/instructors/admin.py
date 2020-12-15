from django.contrib import admin
from instructors.models import Instructor, Position, Coursename, CourseApply
from django.db import models
from django.forms import widgets


class InstructorInline(admin.StackedInline):
    model = Instructor
    fields = ['name']


class PositionAdmin(admin.ModelAdmin):
    inlines = [InstructorInline]


class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'is_active', 'position']
    list_display_links = ['name', 'surname']

    list_filter = ['is_active', 'position']
    search_fields = ['name', 'surname']

    list_editable = ['is_active']

    # fields = ['name', 'surname', 'email', 'data_of_birth', 'position', 'is_active']  # отобразить поля
    # exclude = ['data_of_birth']  # исключить поля
    readonly_fields = ['is_active']  # сделать поле неактивным, для чтения
    raw_id_fields = ['position']

    save_as = True
    save_on_top = True
    
    fieldsets = [
        (None, {'fields': ['name', 'surname']}),
        ('Other information', {'fields': ['email', 'data_of_birth', 'position', 'is_active'], 'classes': ['collapse']}),
    ]

    formfield_overrides = {
        models.DateField: {'widget': widgets.TextInput}
    }


admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Coursename)
admin.site.register(CourseApply)

# Register your models here.
