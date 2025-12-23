import requests
import sqlite3
import json
import time
from datetime import datetime

# === Настройки ===
CLIENT_ID = 'ISD946JN7PFG3353LF7SRG98JAFK6Q16S1M0532VNOOI3IH8224JSV010SU98PJ6'
CLIENT_SECRET = 'I11BVV3AVIMRQGQCVN9LOOGG2VVCBTLKCESSQ3792N79BOGRHS1NEF828TN21UJ9'
REDIRECT_URI = 'https://localhost'


# === Функция получения токена ===
def get_access_token():
    # url = 'https://hh.ru/oauth/token'
    # data = {
    #     'client_id': CLIENT_ID,
    #     'client_secret': CLIENT_SECRET,
    #     'grant_type': 'client_credentials'
    # }
    # response = requests.post(url, data=data)
    # if response.status_code == 200:
    #     return response.json()['access_token']
    # else:
    #     raise Exception(f"Ошибка получения токена: {response.text}")
    return 'APPLNRHL0AMJQU7LI64OVM9ACI0QMOJF7MVBCGE24JQG9L72CQKS9LT4R6ILFLTT'


# === Функция получения вакансий ===
def fetch_vacancies(token, keyword='', area=1, per_page=100, pages=5):
    url = 'https://api.hh.ru/vacancies'
    headers = {'Authorization': f'Bearer {token}'}
    all_vacancies = []

    for page in range(pages):
        params = {
            'text': keyword,
            'area': area,      # 1 — Москва
            'per_page': per_page,
            'page': page
        }
        print(f"Запрос страницы {page + 1}...")
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Ошибка: {response.status_code}")
            break

        data = response.json()
        vacancies = data.get('items', [])
        all_vacancies.extend(vacancies)

        # Защита от лимита запросов
        time.sleep(0.5)

        # Если меньше элементов, чем per_page — значит, это последняя страница
        if len(vacancies) < per_page:
            break

    return all_vacancies


# === Функция сохранения в базу данных ===
def save_to_db(vacancies):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Создание таблицы, если не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hh_vacancies_vacancy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hh_id TEXT UNIQUE,
            name TEXT,
            employer_name TEXT,
            area_name TEXT,
            salary_from REAL,
            salary_to REAL,
            currency TEXT,
            published_at TEXT,
            url TEXT,
            description TEXT
        )
    ''')

    for vac in vacancies:
        try:
            # Получаем детали вакансии
            detail_url = vac['url']
            detail_response = requests.get(detail_url)
            if detail_response.status_code != 200:
                continue
            detail = detail_response.json()

            # Извлекаем данные
            hh_id = vac['id']
            name = vac['name']
            employer_name = vac.get('employer', {}).get('name', '')
            area_name = vac.get('area', {}).get('name', '')
            salary = vac.get('salary', {})
            salary_from = salary.get('from') if salary else None
            salary_to = salary.get('to') if salary else None
            currency = salary.get('currency') if salary else ''
            published_at = vac.get('published_at', '')
            url = vac.get('alternate_url', '')
            description = detail.get('description', '')

            # Вставляем в базу
            cursor.execute('''
                INSERT OR REPLACE INTO hh_vacancies_vacancy (
                    hh_id, name, employer_name, area_name, salary_from, salary_to,
                    currency, published_at, url, description
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                hh_id, name, employer_name, area_name, salary_from, salary_to,
                currency, published_at, url, description
            ))

        except Exception as e:
            print(f"Ошибка при обработке вакансии {vac.get('id')}: {e}")
            continue

    conn.commit()
    conn.close()
    print(f"Сохранено {len(vacancies)} вакансий.")


# === Основная функция ===
def main():
    token = get_access_token()
    print("Токен получен.")

    # Получаем вакансии
    vacancies = fetch_vacancies(token, keyword='', area=1, per_page=100, pages=20)
    print(f"Получено {len(vacancies)} вакансий.")

    # Сохраняем в БД
    save_to_db(vacancies)


if __name__ == '__main__':
    main()
