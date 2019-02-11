import datetime
import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from yatla.twits.models import Twit
from yatla.twits.tests.factories import TwitFactory, LikeFactory, ReTwitFactory
from yatla.users.models import User
from yatla.users.tests.factories import UserFactory


class Command(BaseCommand):
    help = "Creates sample data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--users",
            action="store",
            dest="users",
            type=int,
            help="Number of users created",
        )

    def handle(self, *args, **options):
        User.objects.filter(is_superuser=False).delete()
        Twit.objects.all().delete()
        users = UserFactory.create_batch(size=options["users"] or 100)
        faker = Faker()
        for user in users:
            self.stdout.write(self.style.WARNING(f"Generating timeline for {user}..."))
            twits = [
                TwitFactory(text=faker.text(max_nb_chars=280), user=user)
                for _ in range(random.randint(10, 100))
            ]
            initial = timezone.now()
            for index, twit in enumerate(twits):
                twit.created = initial - (
                    datetime.timedelta(minutes=random.randint(0, 59))
                    + datetime.timedelta(hours=index)
                )
                liked_by = User.objects.order_by("?")[: random.randint(0, len(users))]
                for liked_by_user in liked_by:
                    LikeFactory(user=liked_by_user, twit=twit)
                retwitted_by = User.objects.order_by("?")[
                    : random.randint(0, len(users))
                ]
                for retwitted_by_user in retwitted_by:
                    ReTwitFactory(user=retwitted_by_user, twit=twit)
        self.stdout.write(self.style.SUCCESS(f"Sample data generated!"))
