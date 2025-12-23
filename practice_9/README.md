# Запуск
cd hh_vacancies_project
создание и запуск венв
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python get_data.py
python manage.py runserver