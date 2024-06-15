import os
import django

def setup_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    django.setup()

def append_commands():
    from myapp.models import DjangoCommand
    while True:
        command = input("Enter the command (or type 'exit' to stop appending): ")
        if command.lower() == 'exit':
            break
        description = input("Enter the description: ")
        
        # Save data to DjangoCommand model
        command_obj = DjangoCommand(command=command, description=description)
        command_obj.save()

    print("Data appended to Django commands in the database successfully.")

def main():
    setup_django()
    append_commands()

if __name__ == "__main__":
    main()
