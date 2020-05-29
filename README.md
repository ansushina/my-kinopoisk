# my-kinopoisk

## Стек технологий
* Puthon 3.6 + psycopg2 + Django + Pillow + django-crispy-forms + requests
* Postgresql 
* Bootstrap (установка не требуется)

## Запуск 

Для успешной работы необходимо создать базу данных. Она описана в файле mycourse/settings.py.

### Установка зависимостей 

```
pip3 install -r requirements.txt
```

### Создание миграции 

```
python3 ./manage.py makemigrations
python3 ./manage.py migrate
```

### Создание суперпользователя

```
python3 ./manage.py createsuperuser
```

### Заполнение базы данных 

*Не уверена, что это сработает как должно*

```
ptyhon3 ./manage.py fillDB
```

### Запуск

```
python3 ./manage.py runserver
```

