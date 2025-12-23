from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Vacancy


def vacancy_list(request):
    '''view функция для листа вакансий'''
    query = request.GET.get('q', '')
    area = request.GET.get('area', '')
    min_salary = request.GET.get('min_salary', '')
    max_salary = request.GET.get('max_salary', '')

    vacancies = Vacancy.objects.all()

    if query:
        vacancies = vacancies.filter(name__icontains=query) | vacancies.filter(description__icontains=query)
    if area:
        vacancies = vacancies.filter(area_name__icontains=area)
    if min_salary:
        vacancies = vacancies.filter(salary_from__gte=min_salary)
    if max_salary:
        vacancies = vacancies.filter(salary_to__lte=max_salary)

    paginator = Paginator(vacancies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'area': area,
        'min_salary': min_salary,
        'max_salary': max_salary,
    }

    return render(request, 'hh_vacancies/vacancy_list.html', context)


def vacancy_detail(request, pk):
    '''View функция для страницы деталей вакансии'''
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'hh_vacancies/vacancy_detail.html', {'vacancy': vacancy})