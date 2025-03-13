import os
import time
import psycopg2
from psycopg2 import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Checks the database connection and verifies if it is accessible."

    def handle(self, *args, **kwargs):
        max_try = 5
        self.stdout.write("Checking database connection...")
        while max_try > 0:
            try:
                connection = psycopg2.connect(
                    database = os.getenv("DATABASE_NAME"),
                    user     = os.getenv("DATABASE_USER"),
                    password = os.getenv("DATABASE_PASSWORD"),
                    host     = os.getenv("DATABASE_HOST"),
                    port     = os.getenv("DATABASE_PORT"),
                )

                connection.close()
                self.stdout.write(self.style.SUCCESS("Successfully connected to the database!"))
                break

            except OperationalError as e:
                max_try -= 1
                self.stderr.write(self.style.ERROR(f"Failed to connect to the database: {e}"))

                if max_try > 0:
                    self.stdout.write(self.style.NOTICE(f"Retrying... ({5 - max_try}/5)"))
                    time.sleep(3)

                else:
                    self.stderr.write(self.style.ERROR("Max retries reached. Could not connect to the database."))
                    break
