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

def create_data():
    from college.models import Department, StudentID, Student, Subject, SubjectMark

    # Delete existing records
    SubjectMark.objects.all().delete()
    Subject.objects.all().delete()
    Student.objects.all().delete()
    StudentID.objects.all().delete()
    Department.objects.all().delete()

    # Create Departments
    departments = ['Chemistry', 'Computer Science', 'Mathematics', 'Physics']
    for dep in departments:
        Department.objects.get_or_create(department=dep)

    # Create Subjects
    subjects = [
        ('Chemistry', 'Organic Chemistry', 'CHE101'),
        ('Computer Science', 'Data Structures', 'CSE201'),
        ('Mathematics', 'Calculus', 'MATH101'),
        ('Physics', 'Classical Mechanics', 'PHY101'),
    ]
    for dep_name, subj_name, subj_code in subjects:
        department = Department.objects.get(department=dep_name)
        Subject.objects.create(department=department, subject_name=subj_name, subject_code=subj_code)

    # Create Students
    departments = list(Department.objects.all())
    for _ in range(20):
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

    # Create SubjectMarks
    students = list(Student.objects.all())
    subjects = list(Subject.objects.all())
    for student in students:
        for subject in subjects:
            SubjectMark.objects.create(
                student=student,
                subject=subject,
                mark=random.randint(50, 100)
            )

if __name__ == '__main__':
    print("Creating data...")
    setup_django()
    create_data()
    print("Data created.")
