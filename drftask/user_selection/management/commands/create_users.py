from django.core.management.base import BaseCommand
from user_selection.models import User, Role


class Command(BaseCommand):
     help = 'Создание пользователя'

     def add_arguments(self, parser):
          parser.add_argument('email', type=str, help='Электронная почта пользователя')
          parser.add_argument('password', type=str, help='Пароль для пользователя')
          parser.add_argument('role', type=str, help='Роль пользователя')

     def handle(self, *args, **options):
          email = options['email']
          password = options['password']
          role = options['role']
          
          role_choice = Role.objects.get(name=role)
          user = User.objects.create_user(password=password, email=email, role_choice=role_choice)
          self.stdout.write(self.style.SUCCESS(f'Пользователь {user.email} успешно создан!'))
