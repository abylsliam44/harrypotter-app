import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hp_explorer.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    print('Creating superuser...')
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
else:
    print('Superuser already exists.')
