from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import UserProfile

class Command(BaseCommand):
    help = 'Erstellt fehlende UserProfile-Einträge für Benutzer'

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            if not hasattr(user, 'userprofile'):
                UserProfile.objects.create(user=user)
                self.stdout.write(f"UserProfile created for user: {user.username}")
        self.stdout.write("Fix complete!")
