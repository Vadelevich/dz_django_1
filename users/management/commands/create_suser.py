from django.core.management import BaseCommand

from users.models import User

class Command(BaseCommand):


    def handle(self, *args, **options):
        user = User.objects.create(
            email = 'newtest@sky.pro',
            is_superuser=True
        )

        user.set_password('19941994')
        user.save()
