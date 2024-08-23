from typing import Any
from django.core.management.base import BaseCommand
# from saber.models import Department


class Command(BaseCommand):
    help = 'Populate the database with the data'

    def handle(self, *args, **options):
        self.stdout.write('Seed was called')
