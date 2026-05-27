#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pet_shelter_project.settings')

    if 'RENDER' in os.environ:
        import django
        django.setup()
        from django.contrib.auth import get_user_model
        user_model = get_user_model()
        if not user_model.objects.filter(username='user').exists():
            user_model.objects.create_superuser('user', 'user@admin.com', 'user12345')
            print("=== Superuser 'user' created successfully! ===")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
