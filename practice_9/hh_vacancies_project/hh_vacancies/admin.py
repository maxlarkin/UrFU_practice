from django.contrib import admin
from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    '''регистрация модели Vacancy в админке'''
    list_display = ('name', 'employer_name', 'area_name', 'salary_range', 'published_at')
    search_fields = ('name', 'employer_name', 'area_name')
    list_filter = ('area_name', 'currency')
    # readonly_fields = ('created_at',)

    '''Диапазон зарплат'''
    def salary_range(self, obj):
        if obj.salary_from and obj.salary_to:
            return f"{obj.salary_from} — {obj.salary_to} {obj.currency}"
        elif obj.salary_from:
            return f"от {obj.salary_from} {obj.currency}"
        elif obj.salary_to:
            return f"до {obj.salary_to} {obj.currency}"
        return "Не указана"

    salary_range.short_description = "Зарплата"
