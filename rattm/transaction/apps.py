from django.apps import AppConfig

class TransactionConfig(AppConfig):
    name = 'transaction'

    def ready(self):
        from utils.firebase import db