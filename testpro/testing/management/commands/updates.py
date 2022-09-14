from django.core.management.base import BaseCommand
from testing.models import Student,Book
import pandas as pd
class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # database connection here
        df = pd.read_csv('student.csv')
        for name,roll,city in zip(df.name,df.roll,df.city):
            model=Student(name=name,roll=roll,city=city)
            model.save()