from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Department
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Student, SubjectMark
from django.db.models import Sum

def college(request):
    return HttpResponse('Welcome to College')

def student(request):
    query = request.GET.get('q')
    departments = request.GET.getlist('department')
    age_min = request.GET.get('age_min')
    age_max = request.GET.get('age_max')

    if query == 'None':
        query = None
    if age_min == 'None':
        age_min = None
    if age_max == 'None':
        age_max = None

    students_list = Student.objects.all()

    if query:
        students_list = students_list.filter(student_name__icontains=query)
    if departments:
        students_list = students_list.filter(department__department__in=departments)
    if age_min and age_min.isdigit():
        students_list = students_list.filter(student_age__gte=int(age_min))
    if age_max and age_max.isdigit():
        students_list = students_list.filter(student_age__lte=int(age_max))

    paginator = Paginator(students_list, 10)  # Show 10 students per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    all_departments = Department.objects.all()

    return render(request, 'college/student.html', {
        'page_obj': page_obj,
        'query': query,
        'departments': departments,
        'age_min': age_min,
        'age_max': age_max,
        'all_departments': all_departments
    })

def see_marks(request, student_id):
    queryset = SubjectMark.objects.filter(student__student_id__student_id=student_id)
    total_marks = queryset.aggregate(total_marks=Sum('mark'))['total_marks'] or 0
    return render(request, 'college/see_marks.html', {'queryset': queryset, 'total_marks': total_marks})