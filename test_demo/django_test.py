import os

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
django.setup()
import django.utils.timezone


import datetime

if __name__ == '__main__':
    print(django.utils.timezone.now())
    print(datetime.datetime.now())