from typing import Any
import csv
from django.core.management.base import BaseCommand

from importer.models import get_db

class Command(BaseCommand):
    help = 'This command import data from CSV or JSon files'

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str, help="File you want to Import Data from")
        parser.add_argument('collection_name',type=str,help="The Collection you want to Read datat from")

    def handle(self, *args: Any, **options: Any):
        file_path = options['file_path']
        collection_name = options['collection_name']
        db = get_db()
        if collection_name in db.list_collection_names():
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                db[f"{collection_name}"].insert_many(list(reader))
                self.stdout.write(self.style.SUCCESS("Data Inserted Successfully"))
        else:
            self.stdout.write(self.style.ERROR("Either File Path or Collection Name is invalid"))