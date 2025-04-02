"""
Data Abstraction vs Encapsulation Example in Python

- **Encapsulation**: Hides data using private variables (`__students`).
  - Data cannot be accessed directly from outside the class.
  - Access is provided through a public method (`student()`).
  - Private variables can still be accessed using name mangling (not recommended).

- **Abstraction**: Hides implementation details and provides only necessary functionality.
  - Typically achieved using abstract classes (`ABC`) and abstract methods.
  - This script now includes both encapsulation and abstraction examples.
"""

from abc import ABC, abstractmethod

# Abstraction Example
class Course(ABC):  # Abstract class
    @abstractmethod
    def student(self):
        pass  # Abstract method, must be implemented in subclasses

class Ineuron(Course):
    __students = "Data Science"  # Private variable (Encapsulation)
    
    def student(self):
        """Public method to access private data"""
        print("Class of students:", Ineuron.__students)

# Creating an instance of Ineuron
i = Ineuron()
print(i)  # Printing object reference

i.student()  # Accessing private data using a method

# Trying to access private variable directly (not recommended)
# This is possible due to name mangling but should be avoided
print(i._Ineuron__students)  # Accessing private variable forcefully
