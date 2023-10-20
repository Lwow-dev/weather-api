# weather-api
Test task project

Для запуска приложения после клонирования репозитория необходимо:

1. Создать виртуальное окружение (для linux Ubuntu: python3 -m venv env) 
2. Активировать виртуальное окружение (для linux Ubuntu: source env/bin/activate)
3. Установить зависимости из файла requirements.txt (pip install -r requirements.txt)
4. В папке проекта (рядом с manage.py) создать файл .env, содержащий следующие переменные:
     SECRET_KEY=YUOR_DJANGO_SECRET_KEY
    API_GEOCODER=YUOR_YANDEX_GEOCODER_API_KEY
    API_WEATHER=YUOR_YANDEX_WEATHER_API_KEY
    DOMAIN=YOUR_WORK_DOMAIN
5. Настроить подключение к базе данных (стандартно sqlite)
6. Сделать миграции (python manage.py makemigration ; python manage.py migrate)
7. Тестово запустить приложение (python manage.py runserver)
8. Чтобы запустить приложение на продакшн с помощью gunicorn можно использовать туториал https://habr.com/en/articles/546778/

Хорошей погоды в доме!
