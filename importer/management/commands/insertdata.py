from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This Command allows to insert data from csv or json"

    def handle(self, *args: Any, **options: Any):
        self.stdout.write(self.style.SUCCESS("Data Inserted"))