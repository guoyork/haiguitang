from django.core.management.base import BaseCommand
from user_inputs.models import Rating, QA

class Command(BaseCommand):
    help = 'Clear all Rating instances from database'

    def handle(self, *args, **options):
        count = Rating.objects.count()
        Rating.objects.all().delete()
        QA.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} Rating instances'))
