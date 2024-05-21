from django.core.management.base import BaseCommand
from users.models import User, Request

class Command(BaseCommand):
    help = 'Exports user email addresses to a text file'

    def handle(self, *args, **options):
        
        filename = "export_users_email.txt"
        with open(filename, 'w') as file:
            
            for user in User.objects.all():
                email = user.email
                if email:
                    file.write(email + '\n')
        self.stdout.write(self.style.SUCCESS(f'Successfully wrote emails to {filename}'))

        filename = "request__email.txt"
        with open(filename, 'w') as file:
            
            for user in Request.objects.all():
                email = user.email
                if email:
                    file.write(email + '\n')
        self.stdout.write(self.style.SUCCESS(f'Successfully wrote emails to {filename}'))
