import os
import django

def setup_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    django.setup()

def populate_commands():
    from myapp.models import DjangoCommand
    commands_data = [
        {'command': 'django-admin startproject myproject', 'description': 'Creating a New Project'},
        {'command': 'python manage.py startapp myapp', 'description': 'Creating a New App'},
        {'command': 'python manage.py runserver', 'description': 'Running the Development Server'},
        {'command': 'python manage.py makemigrations', 'description': 'Making Migrations'},
        {'command': 'python manage.py migrate', 'description': 'Applying Migrations'},
        {'command': 'python manage.py createsuperuser', 'description': 'Creating a Superuser'},
        {'command': 'python manage.py changepassword admin', 'description': 'Resetting Admin Password'},
        {'command': 'python manage.py shell', 'description': 'Starting the Django Python Shell'},
    ]

    DjangoCommand.objects.all().delete()

    for data in commands_data:
        command_obj = DjangoCommand(command=data['command'], description=data['description'])
        command_obj.save()

    print("Django commands data overwritten in the database successfully.")

def populate_features():
    from myapp.models import Feature
    features_data = [
        {'name': 'Fast', 'detail': 'This is a fast feature', 'is_true': True, 'icon': 'bi bi-gem'},
        {'name': 'Secure', 'detail': 'This is a secure feature', 'is_true': True, 'icon': 'bi bi-lock'},
        {'name': 'Reliable', 'detail': 'This is a reliable feature', 'is_true': False, 'icon': 'bi bi-book'},
        {'name': 'Scalable', 'detail': 'This is a scalable feature', 'is_true': True, 'icon': 'bi bi-arrows-expand'},
    ]

    Feature.objects.all().delete()

    for data in features_data:
        feature_obj = Feature(name=data['name'], detail=data['detail'], is_true=data['is_true'], icon=data['icon'])
        feature_obj.save()

    print("Features data overwritten in the database successfully.")

def main():
    setup_django()
    populate_commands()
    populate_features()

if __name__ == "__main__":
    main()
