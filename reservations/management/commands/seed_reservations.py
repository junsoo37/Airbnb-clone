import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from django_seed import Seed

from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):
    help = "This command creates reservations"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help="How many reservations you want to create")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "check_in": lambda x: timezone.now().date()+timedelta(days=random.randint(0, 3)),
                "check_out": lambda x: timezone.now().date()+timedelta(days=random.randint(4, 25)),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms)
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Reservations created"))
