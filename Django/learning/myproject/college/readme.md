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


## Django ORM Aggregation and Annotation

### Aggregation

Aggregation in Django is used to compute values such as sums, averages, counts, etc., across querysets. The `aggregate()` method is used to apply aggregation functions to the queryset.

#### Example

Calculate the average age of students in the 'Chemistry' department:

```python
from django.db.models import Avg

# Calculate the average age of students in the 'Chemistry' department
average_age = Student.objects.filter(department__department='Chemistry').aggregate(Avg('student_age'))

print(average_age)  # Output will be a dictionary: {'student_age__avg': <average_age>}
```
### Other Aggregation Functions
- Count: Counts the number of items in a queryset.
- Max: Finds the maximum value in a queryset.
- Min: Finds the minimum value in a queryset.
- Sum: Sums up the values in a queryset.

#### Example

```python
from django.db.models import Count, Max, Min, Sum

# Count the number of students in the 'Chemistry' department
student_count = Student.objects.filter(department__department='Chemistry').aggregate(Count('id'))

# Find the maximum age of students in the 'Chemistry' department
max_age = Student.objects.filter(department__department='Chemistry').aggregate(Max('student_age'))

# Find the minimum age of students in the 'Chemistry' department
min_age = Student.objects.filter(department__department='Chemistry').aggregate(Min('student_age'))

# Sum the ages of students in the 'Chemistry' department
total_age = Student.objects.filter(department__department='Chemistry').aggregate(Sum('student_age'))
```


### Annotation
Annotation in Django is used to add calculated fields to your querysets. The annotate() method is used to add these calculated fields.

#### Example

Annotate each department with the count of students in that department:


```python
from django.db.models import Count

# Annotate each department with the count of students in that department
departments = Department.objects.annotate(student_count=Count('depart'))

for department in departments:
    print(department.department, department.student_count)

```

### Combining Annotation with Aggregation


You can combine annotation with aggregation to perform more complex queries. For instance, let's annotate each department with the average age of students and count of students in that department.

```python
from django.db.models import Avg

# Annotate each department with the average age of students and count of students in that department
departments = Department.objects.annotate(average_age=Avg('depart__student_age'), student_count=Count('depart'))

for department in departments:
    print(department.department, department.average_age, department.student_count)
```


### Summary
- Aggregation: Use aggregate() to calculate values like sum, average, count, etc., across a queryset.
- Annotation: Use annotate() to add calculated fields to your querysets.
- Combining: You can combine aggregation and annotation to perform more complex queries and calculations.


For more queries, refer to the [Django QuerySet API reference](https://docs.djangoproject.com/en/5.0/ref/models/querysets/).