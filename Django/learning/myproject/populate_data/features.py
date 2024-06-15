import os
import sys
import django

def setup_django():
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(project_path)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    django.setup()
def append_features():
    from myapp.models import Feature
    while True:
        name = input("Enter the feature name (or type 'exit' to stop appending): ")
        if name.lower() == 'exit':
            break
        detail = input("Enter the feature detail: ")
        is_true = input("Is it true (True/False): ").lower() == 'true'
        icon = input("Enter the icon name: ")
        
        # Save data to Feature model
        feature_obj = Feature(name=name, detail=detail, is_true=is_true, icon=icon)
        feature_obj.save()

    print("Data appended to Features in the database successfully.")

def main():
    setup_django()
    append_features()

if __name__ == "__main__":
    main()
