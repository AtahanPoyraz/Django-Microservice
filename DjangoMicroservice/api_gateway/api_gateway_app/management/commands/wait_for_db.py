from django.core.management.base import BaseCommand
import psycopg2
import os
from dotenv import load_dotenv
from django.conf import settings
import time

class Command(BaseCommand):
    help = 'Wait for the database to become available.'

    def handle(self, *args, **kwargs):
        load_dotenv(settings.ENVIRONMENT_FILE)

        self.stdout.write("Waiting for the database...")

        database_status = False
        while not database_status:
            try:
                with psycopg2.connect(
                    database=os.environ.get("DATABASE_NAME"),
                    user=os.environ.get("DATABASE_USER"),
                    password=os.environ.get("DATABASE_PASSWORD"),
                    host=os.environ.get("DATABASE_HOST"),
                    port=os.environ.get("DATABASE_PORT")
                ) as conn:
                    database_status = True
                    self.stdout.write(self.style.SUCCESS("Database connection successful!"))

            except KeyboardInterrupt:
                self.stderr.write("Database connection interrupted by user.")
                break

            except Exception as e:
                self.stderr.write(f"Database unavailable: {e}")
                time.sleep(5)