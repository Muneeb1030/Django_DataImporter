from typing import Any
from django.core.management.base import BaseCommand

from importer.models import get_db
import pandas as pd

import datetime
class Command(BaseCommand):
    help= "This command will allow to export mongo db data as csv"

    def add_arguments(self, parser):
        parser.add_argument('collection_name',type=str, help="Model name you want to export data from")

    def handle(self, *args: Any, **options: Any):
        collection_name = options['collection_name']
        db = get_db()
        if collection_name in db.list_collection_names():
           
            df = pd.DataFrame(list(db[f'{collection_name}'].find({},{"_id":0})))
            df.to_csv(f'{collection_name}_data_eportedAt_{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")}')
            self.stdout.write(self.style.SUCCESS("Data Exported Successfully"))
        else:
            self.stdout.write(self.style.ERROR("Collection Name is invalid"))