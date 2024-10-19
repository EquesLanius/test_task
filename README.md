# Последовательность исполнения:
* развертывание с помощью: docker-compose up
* создать тестового суперпользователя с помощью django command: init_su
* создать роли с помощью django command: create_roles
* создать пользователей с помощью django command: create_users
* использовать реализованные эндпоинты

# Django commands:
* init_su - быстрое создание тестового суперпользователя.
* команда для исполнения: python manage.py init_su
* log: 'root@root.com' psw: 'admin' - данные для авторизации на django admin

* create_roles - создание ролей user, manager, crm-admin.  
* команда для исполнения:  python manage.py create_roles

* create_users - создание пользователей, доступные роли: user, manager, crm-admin.
* команда для исполнения: python manage.py create_users email password role

# Маршруты доступные в API:
* api/users/ - создание нового пользователя
* api/users/user_id - получение пользователя по его id