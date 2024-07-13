# Django ORM Queries

Below are some Django ORM queries for reference, along with their descriptions.


```python
# Filter students whose name starts with 'a'
# This query will return all students whose names begin with the letter 'a'.
Student.objects.filter(student_name__startswith="a")

# Filter students whose email ends with '.org'
# This query will return all students whose email addresses end with '.org'.
Student.objects.filter(student_email__endswith=".org")

# Filter students whose name contains 'an'
# This query will return all students whose names contain the substring 'an'.
Student.objects.filter(student_name__icontains="an")

# Filter students whose department contains 'Chemistry'
# This query will return all students who belong to a department with 'Chemistry' in its name.
Student.objects.filter(department__department__icontains="Chemistry")

# Count students whose department is in ['Chemistry']
# This query will count the number of students who belong to the 'Chemistry' department.
Student.objects.filter(department__department__in=["Chemistry"]).count()

# Check if there are any students whose department is in ['Chemistry']
# This query will return True if there are any students in the 'Chemistry' department, otherwise False.
Student.objects.filter(department__department__in=["Chemistry"]).exists()

# Reverse the order of students whose department is in ['Chemistry']
# This query will return students in the 'Chemistry' department in reverse order of their IDs.
Student.objects.filter(department__department__in=["Chemistry"]).reverse()

# Order students by age whose department is in ['Chemistry']
# This query will return students in the 'Chemistry' department ordered by their age in ascending order.
Student.objects.filter(department__department__in=["Chemistry"]).order_by("student_age")

# Get values of students whose department is in ['Chemistry']
# This query will return a list of dictionaries containing field values for students in the 'Chemistry' department.
Student.objects.filter(department__department__in=["Chemistry"]).values()

# Get a list of department and student names for students whose department is in ['Chemistry']
# This query will return a list of tuples with department names and student names for students in the 'Chemistry' department.
Student.objects.filter(department__department__in=["Chemistry"]).values_list("department__department", "student_name")

# Get distinct departments of students whose department is in ['Chemistry']
# This query will return distinct department names for students in the 'Chemistry' department.
Student.objects.filter(department__department__in=["Chemistry"]).distinct()
```

For more queries, refer to the [Django QuerySet API reference](https://docs.djangoproject.com/en/5.0/ref/models/querysets/).