import os
from celery.schedules import crontab
from celery import Celery, shared_task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NoFap_project.settings')

app = Celery('NoFap_project', broker='pyamqp://guest@localhost//', backend='rpc://')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@shared_task
def chegou_setembro():
  from Core_app.views import toggle_EH_SETEMBRO
  toggle_EH_SETEMBRO()



@app.on_after_configure.connect
def load_setup_periodic_task(sender:Celery, **kw:dict):
  sender.add_periodic_task(
    crontab(),
    chegou_setembro.s(),
    name='chegou setembro',
  )

