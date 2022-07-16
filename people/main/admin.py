from django.contrib import admin
from .models import People, City, Job


@admin.register(People)
class People(admin.ModelAdmin):
    """Информация о человеке"""
    list_display = 'name', 'id', 'age', 'city', 'job', 'email',
    list_filter = 'city', 'job',
    fieldsets = (
        ('ОСНОВНЫЕ ДАННЫЕ', {'fields': ('name', 'age',)}),
        ('ДОПОЛНИТЕЛЬНЫЕ ДАННЫЕ', {'fields': ('city', 'job', 'email',)}),
    )


@admin.register(City)
class City(admin.ModelAdmin):
    """Город"""
    list_display = 'name', 'count_people',


@admin.register(Job)
class Job(admin.ModelAdmin):
    """Работа"""
    list_display = 'name', 'count_people',
