from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from viz.models import TMDB
from pytz import UTC


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from tmdb_results.csv into our TMDB model"

    def handle(self, *args, **options):

        if TMDB.objects.exists():
            print('TMDB data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("Loading TMDB data")
        for row in DictReader(open('./tmdb_results.csv', encoding='latin-1')):
            tmdb = TMDB()
            tmdb.popularity = row['popularity']
            tmdb.vote_count = row['vote_count']
            tmdb.movie_id = row['movie_id']
            tmdb.title = row['title']
            tmdb.vote_average = row['vote_average']
            tmdb.description = row['description']

            raw_release_date = row['release_date']
            release_date = UTC.localize(datetime.strptime(raw_release_date, "%m/%d/%y"))
            tmdb.release_date = release_date
            tmdb.save()

