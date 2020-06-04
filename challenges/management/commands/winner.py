from django.core.management.base import BaseCommand, CommandError
from rifas.models import Rifa, Ticket
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Pick winner'

    def handle(self, *args, **options):
      import random
      import datetime
      rifas = Rifa.objects.filter(winner=None,end_date__lt=datetime.date.today())
      for rifa in rifas:
        tickets = Ticket.objects.filter(rifa=rifa).all()
        winner = tickets[random.randint(0,len(tickets))]
        rifa.winner = User.objects.get(pk=winner.user_id)
        rifa.winner_phone = winner.phone
        rifa.save()
        self.stdout.write(self.style.SUCCESS('Successfully closed item "%s" winner: "%s' % (rifa,winner,)))

      self.stdout.write(self.style.SUCCESS('Successfully closed all items'))