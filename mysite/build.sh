#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r mysite/requirements.txt

# Convert static asset files
python mysite/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python mysite/manage.py migrate && 
python mysite/manage.py createsuperuser --no-input || 
echo "Superuser already exists"

