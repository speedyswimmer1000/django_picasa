#! /usr/bin/env python

from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taggerProject.settings')
app = Celery('taggerProject',broker = settings.CELERY_BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request) )

