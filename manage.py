#!/usr/bin/env python
from django.conf import settings

import os
import sys
import django
import django.conf as conf

if __name__ == '__main__':

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_rosamistica.settings')

    try:

        django.setup()
        # Override default port for `runserver` command
        from django.core.management.commands.runserver import Command as runserver
        runserver.default_port = "8003"

        #conf.settings.DATABASES['default']['NAME'] = 'djangodb_rosamistica'
        conf.settings.DATABASES['default']['NAME'] = 'rosamisticadb'

        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)
