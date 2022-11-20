from ..NoFap_project.celery import app
from celery import shared_task
from celery import Celery
from celery.schedules import crontab

from .views import EH_SETEMBRO



