import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

def create_superuser(username, email, password):
    if User.objects.filter(username=username).exists():
        print('Superuser already exists')
    else:
        User.objects.create_superuser(username=username, email=email, password=password)
        print('Superuser created successfully')

if __name__ == '__main__':
    create_superuser('andrew', 'drewkallmeyer@gmail.com', 'tessa123')