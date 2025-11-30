from abc import abstractmethod, ABC

# ======= PRACTICE 1 ======= 
class Shape(ABC):
    """Calculates the total area of a collection of shapes."""
    def __init__(self, shapes: list['Shape']):
        self.shapes = shapes

    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__([])
        self.radius = radius
        
    def calculate_area(self) -> float:
        return 3.14159 * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, height: float, width: float):
        super().__init__([])
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        return self.height * self.width
    
    
class Triangle(Shape):
    def __init__(self, length: float):
        super().__init__([])
        self.length = length

    def calculate_area(self) -> float:
        return 0.5 * self.length * self.length


class Square(Shape):
    def __init__(self, height: float):
        self.height = height
    
    def calculate_area(self) -> float:
        return self.height * self.height


class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    def calculate_total_area(self) -> float:
        total = 0.0
        for shape in self.shapes:
            total += shape.calculate_area()
        return total

# ======= PRACTICE 2 ======= 

class Employee(ABC):
    """Abstract base class for all employee types."""
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_salary(self) -> int:
        """Defines the contract for salary calculation."""
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self) -> int:
        return 5000


class PartTimeEmployee(Employee):   
    def calculate_salary(self) -> int:
        return 3000


class InternEmployee(Employee):
    def calculate_salary(self) -> int:
        return 1000


if __name__ == "__main__":
    
    # Practice 1
    shapes_ocp: list[Shape] = [
        Circle(5),
        Rectangle(4, 5),
        Triangle(3),
        Square(5)
    ]
    area_calc = AreaCalculator(shapes_ocp)
    print(f"Practice 1 (OCP Compliant): Total Area = {area_calc.calculate_total_area():.2f}")
    
    # Practice 2
    full_time_employee_ocp = FullTimeEmployee("Alice",)
    print(f"Practice 2 (OCP Compliant): {full_time_employee_ocp.name}'s salary is {full_time_employee_ocp.calculate_salary()}")

    intern_employee_ocp = InternEmployee("Bob")
    print(f"Practice 2 (OCP Compliant): {intern_employee_ocp.name}'s salary is {intern_employee_ocp.calculate_salary()}")