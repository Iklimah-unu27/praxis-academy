"""
WSGI config for fish project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fish.settings')

application = get_wsgi_application()

# bikin primary key ama foreign key biar bisa nyambung
# benenrin nomer 
# bikin halaman login
# benerin data tabel biar keliatan relasinya