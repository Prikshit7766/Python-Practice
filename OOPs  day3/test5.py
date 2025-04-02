"""
Data Abstraction Example in Python

- **Abstraction**: Hides implementation details and provides only necessary functionality.
  - Achieved using abstract classes (`ABC`) and abstract methods (`@abstractmethod`).
  - Subclasses must implement the abstract methods, enforcing a contract.
  
- **@abstractmethod**: A decorator that ensures the method must be implemented in any subclass.
  - If a subclass does not provide an implementation, it cannot be instantiated.
  
- **What happens if we don't inherit from `ABC`?**
  - If we only import `abc` and use `@abstractmethod` **without inheriting `ABC`**, the subclass is **not forced** to implement the method.
  - The abstract method becomes a normal method with no enforcement.
  
- **Can we still call `student()` if we don't inherit `ABC`?**
  - Yes! Since `@abstractmethod` is ignored, the method behaves like a regular method.
  - Calling `obj.student()` does not raise an error but simply executes the base class implementation.
  - Since the base class method contains only `pass`, it runs but does nothing.
  - This defeats the purpose of abstraction, as the method is not actually enforced.
"""

from abc import ABC, abstractmethod
import abc

# Correct abstraction using ABC
class Course(ABC):
    @abstractmethod
    def student(self):
        """Abstract method that must be implemented in subclasses"""
        pass

# Concrete class implementing abstraction
class Ineuron(Course):
    def student(self):
        """Implementation of the abstract method"""
        print("Class of students: Data Science")

# Creating an instance of Ineuron
i = Ineuron()
print(i)  # Printing object reference

i.student()  # Calling the implemented abstract method

# Incorrect abstraction without ABC inheritance
class CourseWithoutABC:
    @abc.abstractmethod
    def student(self):
        """Abstract method that should be implemented but is NOT enforced"""
        pass

# Subclass without implementing student()
class IneuronWithoutEnforcement(CourseWithoutABC):
    pass  # No error, since CourseWithoutABC is not an actual abstract class

# Creating an instance without implementing the abstract method
obj = IneuronWithoutEnforcement()  # No error, method enforcement is bypassed
print(obj)  # Works fine

# Calling student() still works and executes the base class implementation (which is just `pass`)
obj.student()  # No error, runs the empty base class method