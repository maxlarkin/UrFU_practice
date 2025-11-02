from django.shortcuts import render
from requests import get


# Create your views here.
def dog_list(request):
    """Получение всех пород"""
    all_breeds = get('https://dog.ceo/api/breeds/list/all').json()['message']
    images_data = []

    """Получение изображений для каждой породы"""
    if request.GET:
        images_data = [{
            'images': get(f'https://dog.ceo/api/breed/{breed}/images/random/3').json()['message'],
            'breed': breed
            } for breed in request.GET['breeds'].split(', ')]

    """Рендер страницы с информацией о породе"""
    return render(request, 'dog_info/dog_info_temp.html',
                  {'all_breeds': all_breeds, 'images_data': images_data})
