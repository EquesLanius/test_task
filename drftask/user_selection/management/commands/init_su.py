from django.core.management.base import BaseCommand
from user_selection.models import User

class Command(BaseCommand):
     help = 'Создание суперпользователя'

     def handle(self, *args, **options):
          User.objects.create_user(
               email='root@root.com',
               password='admin',
               is_staff=True,
               is_active=True,
               is_superuser=True
          )
          self.stdout.write(self.style.SUCCESS(f'Суперпользователь успешно создан!'))