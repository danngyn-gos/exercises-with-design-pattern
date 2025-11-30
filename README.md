# Exercises with Design Patterns - SOLID Principles

A hands-on exercise repository for learning and practicing SOLID design principles through Python refactoring exercises.

## 📚 SOLID Principles

1. **S - Single Responsibility Principle (SRP)**: Every class should have a single responsibility
2. **O - Open/Closed Principle (OCP)**: Open for extension, closed for modification
3. **L - Liskov Substitution Principle (LSP)**: Derived classes must be substitutable for their base classes
4. **I - Interface Segregation Principle (ISP)**: Make fine-grained, client-specific interfaces
5. **D - Dependency Inversion Principle (DIP)**: Depend on abstractions, not concretions

## 🎯 Goal

Refactor code in each exercise folder to follow the corresponding SOLID principle and write comprehensive tests.
```
exercises-with-design-pattern/
├── Solid/
│ ├── Srp/ # Single Responsibility Principle
│ ├── Ocp/ # Open/Closed Principle
│ ├── Lsp/ # Liskov Substitution Principle
│ ├── Isp/ # Interface Segregation Principle
│ └── Dip/ # Dependency Inversion Principle
└── tests/
└── Spr/ # Test files
```

Each exercise folder contains:
- `main.py` - Python implementation to refactor

🧪 Testing
Run Python tests:
```
python -m unittest tests.Spr.test
```
Or from the test directory:

```
cd tests/Spr
python test.py
```