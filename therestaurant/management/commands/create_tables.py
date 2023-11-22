from django.core.management.base import BaseCommand
from therestaurant.models import Table


class Command(BaseCommand):
    help = 'Creates tables with table number and covers.'

    def handle(self, *args, **kwargs):
        tables = [
            Table(table_number=1, table_covers=1),
            Table(table_number=2, table_covers=1),
            Table(table_number=3, table_covers=1),
            Table(table_number=4, table_covers=1),
            Table(table_number=5, table_covers=1),
            Table(table_number=6, table_covers=2),
            Table(table_number=7, table_covers=2),
            Table(table_number=8, table_covers=4),
            Table(table_number=9, table_covers=4),
            Table(table_number=10, table_covers=4)
        ]

        for table in tables:
            table.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 10 Table objects.'))
