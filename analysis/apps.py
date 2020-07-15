from django.apps import AppConfig
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from . import views
import logging


class AnalysisConfig(AppConfig):
    name = 'analysis'

    def ready(self):
        logger = logging.getLogger(__name__)
        logger.warning("STARTING SCHEDULER")
        from scheduler import update
        update.start()