from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
         user = User.objects.get(pk=3)
         group, created = Group.objects.get_or_create(
             name="profile-manager",
         )
         permissions_profile = Permission.objects.get(
             codename="view_profile",
         )

         permissions_logentry = Permission.objects.get(
             codename="view_logentry",
         )

        # добавление разрешения в группу
         group.permissions.add(permissions_profile)

        # добавление пользователя к группе
         user.groups.add(group)

         # добавления пользователя напрямую с разрешением
         user.user_permissions.add(permissions_logentry)

         group.save()
         user.save()