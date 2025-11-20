from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data (delete one by one)
        for obj in Activity.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in User.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Team.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Workout.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Leaderboard.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Users
        spider = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        iron = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Activities
        Activity.objects.create(user=spider, type='Running', duration=30, date='2025-11-20')
        Activity.objects.create(user=iron, type='Cycling', duration=45, date='2025-11-19')
        Activity.objects.create(user=batman, type='Swimming', duration=60, date='2025-11-18')
        Activity.objects.create(user=superman, type='Flying', duration=120, date='2025-11-17')

        # Workouts
        Workout.objects.create(name='Hero Training', description='Intense workout for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Power Lifting', description='Strength workout for DC heroes', suggested_for='DC')

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=175, position=1)
        Leaderboard.objects.create(team=dc, points=180, position=2)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
