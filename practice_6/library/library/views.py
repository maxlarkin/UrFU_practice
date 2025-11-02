from django.shortcuts import render


def books_detail(request):
    """
    View-функция для отображения детальной информации о книге
    """
    # Получаем книги
    books = [
        {
            'title': 'Book 1',
            'content': 'something content 1',
            'published_year': '1982',
            'author': 'someone 1',
            'is_available': True
        },
        {
            'title': 'Book 2',
            'content': 'something content 2',
            'published_year': '2123',
            'author': 'someone 2',
            'is_available': False
        }
    ]

    return render(request, 'library/book_detail.html', {"books": books})
