from django.core.management.base import BaseCommand
from user_selection.models import Role
from django.core.files import File


class Command(BaseCommand):
     help = 'Создание ролей'

     def handle(self, *args, **options):
          avatars = ['user_GloECTD_A6RfMVz.png', 'manager_7vNhf4m_y0088q6.png', 'crm_admin_ZRldxPT_U13wSJw.png']
          roles = ['user', 'manager', 'crm_admin']

          for info in zip(avatars, roles):
               with open(f'media/avatars/{info[0]}', 'rb') as f: 
                    role = Role(name=info[1])
                    role.avatar.save(info[0], File(f)) 
                    role.save()

          self.stdout.write(self.style.SUCCESS(f'Роли успешно созданы!'))