Маршруты доступные в API:
     api/users/ - создание нового пользователя
     api/users/user_id - получение пользователя по его id


Также с помощью django command - create_users можно создавать пользователей,
роли доступные для создания пользователя: user, manager, crm-admin.

Переходим в директорию проекта:
     cd drftask
Шаблон команды для исполнения:
     python manage.py create_users <email> <password> <role>

p.s Таблица Role заполняется суперадмином, три роли: user, manager, crm-admin.
Аватары для каждой роли находятся в media/avatars   