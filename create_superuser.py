import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laundry.settings")
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin1", "admin@example.com", "admin1234")
    print("Superuser created.")
else:
    print("Superuser already exists.")
