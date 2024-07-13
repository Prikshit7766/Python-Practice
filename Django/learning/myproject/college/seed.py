import os
import django
import random
import sys
from faker import Faker

def setup_django():
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(project_path)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    django.setup()

fake = Faker()

def create_students(num_students=10):
    from college.models import Department, StudentID, Student
    departments = list(Department.objects.all())
    for _ in range(num_students):
        department = random.choice(departments)
        student_id = StudentID.objects.create(student_id=fake.unique.random_number(digits=8))
        student = Student.objects.create(
            department=department,
            student_id=student_id,
            student_name=fake.name(),
            student_email=fake.unique.email(),
            student_age=random.randint(18, 30),
            student_phone=fake.phone_number(),
            student_address=fake.address()
        )
        print(f'Student {student.student_name} created.')

if __name__ == '__main__':
    print("Creating students...")
    setup_django()
    create_students(20)  # Create 20 students
    print("Students created.")


# Chemistry
# Computer Science
# Mathematics
# Physics