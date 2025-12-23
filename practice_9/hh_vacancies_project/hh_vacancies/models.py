from django.db import models


class Vacancy(models.Model):
    '''Модель вакансии для бд'''
    hh_id = models.CharField(max_length=50, unique=True, verbose_name="ID на HH")
    name = models.CharField(max_length=500, verbose_name="Название")
    employer_name = models.CharField(max_length=300, blank=True, verbose_name="Работодатель")
    area_name = models.CharField(max_length=100, blank=True, verbose_name="Город")
    salary_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="ЗП от")
    salary_to = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="ЗП до")
    currency = models.CharField(max_length=10, blank=True, verbose_name="Валюта")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата публикации")
    url = models.URLField(blank=True, verbose_name="Ссылка на HH")
    description = models.TextField(blank=True, verbose_name="Описание")

    '''Мета информация модели'''
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    '''текстовое представление'''
    def __str__(self):
        return f"{self.name} ({self.employer_name})"