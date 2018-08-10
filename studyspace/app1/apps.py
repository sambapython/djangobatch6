# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'app1'

    def ready(self):
    	from app1.signals import save_profile

