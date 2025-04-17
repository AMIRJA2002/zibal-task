from apps.transactions.selectors import get_daily_transactions, get_weekly_transactions, get_monthly_transactions
from apps.transactions.models import TransactionSummary
from django.core.management import BaseCommand
from mongoengine import disconnect, ConnectionFailure
from mongoengine import connect
from datetime import datetime


class Command(BaseCommand):
    help = 'Update transaction summary (amount & count) for daily, weekly, monthly'

    def handle(self, *args, **options):
        self.get_connection()

        modes = ['daily', 'weekly', 'monthly']

        for mode in modes:
            summary_doc = TransactionSummary.objects(mode=mode).first()
            if summary_doc:
                TransactionSummary.objects(mode=mode).delete()

            summary_doc = TransactionSummary(
                mode=mode,
                summary=self.get_function(mode)(type='amount'),
                lastUpdate=datetime.now()
            )
            summary_doc.save()

    def get_function(self, mode):
        modes = {
            'daily': get_daily_transactions,
            'weekly': get_weekly_transactions,
            'monthly': get_monthly_transactions
        }
        return modes[mode]

    def get_connection(self):
        disconnect()
        db = connect(
            db="zibal_db",
            host="mongodb://localhost:27017/zibal_db"
        )
        return db

