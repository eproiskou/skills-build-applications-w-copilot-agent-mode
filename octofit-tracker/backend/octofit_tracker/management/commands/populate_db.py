from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name)

        # Create activities
        Activity.objects.create(user=tony.email, activity_type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user=steve.email, activity_type='cycle', duration=45, date='2023-01-02')
        Activity.objects.create(user=bruce.email, activity_type='swim', duration=60, date='2023-01-03')
        Activity.objects.create(user=clark.email, activity_type='fly', duration=120, date='2023-01-04')

        # Create leaderboard
        Leaderboard.objects.create(user=tony.email, score=100)
        Leaderboard.objects.create(user=steve.email, score=90)
        Leaderboard.objects.create(user=bruce.email, score=110)
        Leaderboard.objects.create(user=clark.email, score=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')
        Workout.objects.create(name='Squats', description='Do 40 squats')
        Workout.objects.create(name='Plank', description='Hold for 1 minute')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
