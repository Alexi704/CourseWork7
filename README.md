# проект: "Calendar"
___
## стек (python3.9, Django, Postgres)
___
**ЗАПУСК:** 
1. Скачать проект
2. Установить зависимости: 
0.[ ] pip install -r requirements.txt
3. Прописать в .env свои логины/пароли
4. Установить докер. Создать докер-контейнер, например:
0.[ ] docker run --name todolist_cw7 -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
5. Накатить миграции:
0.[ ] python manage.py makemigrations
0.[ ] python manage.py migrate
6. Запустить проект
0.[ ] python manage.py runserver