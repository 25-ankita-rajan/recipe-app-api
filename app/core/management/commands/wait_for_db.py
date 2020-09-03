import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution untill databse is available"""

    def handle(self, *args, **options):
        self.stdout.write('waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('database unavailable, waiting 1 seccond...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('database available!'))
