# Зависимости
Для установки рекомендуется создать виртуальное окружение с Python версии 1.12
Все необходимые зависимости перечислены в файле requirements.txt:
```py
pip -r requirements.txt
```
Проект использует базу данных PostgreSQL.
# Разворачивание сервера
## 1. Инициализация базы данных
Запускаем службу postgresql для запуска базы данных или используем приложенный Docker контейнер:
```
docker compose up
```

Создаём новую БД в postgres или указываем в файле PlywoodTickets/settings.py новые данные для доступа:
```
NAME: flywood_db
USER: postgres
PASSWORD: 0000
``` 

Дальне необходимо выполнить миграции. На Linux для этого достаточно вызвать bash-скрипт reset_migrations из корневой папки.
На остальных ОС или в случае, если скрипт не работает, из директории PlywoodTickets выполняем следующие команды:
```py
python manager.py makemigrations mainpage
python manager.py makemigrations personalLocker
python manager.py migrate
```

В случае изменения модели связей между таблицами БД необходимо полностью удалять каталоги __pycache__ и migrations из проекта и повтороно выполнять команды выше.
Данный случай также обрабатывается скриптом reset_migrations.

## 2. Инициализация сервера
Переходим в директорию ml и запускаем сервер ИИ:
```
python service.py
```
Открываем новую сессию в консоли, переходим в директорию PlywoodTickets и запускаем сам сервер:
```py
python manage.py runserver
```

Теперь серверр Backend работает и ожидает запросов

# Памятка
Фронт: [https://github.com/LongDude/Hotfix2024-Front](https://github.com/LongDude/Hotfix2024-Front)

Порт фронта: 3000

Порт бека: 8000

Порт pgadmin (при разворачивании докера): 8080

Все сервера на данный момент работают в локальной сети
