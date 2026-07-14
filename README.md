# Inventory Manager

A simple inventory control system built as a hands-on learning project. It started as a way to practice Python fundamentals and grew step by step as I studied more advanced concepts — object-oriented programming, decorators, context managers, and proper project structuring.

The project is based on a learning roadmap, and I plan to keep evolving it as I go through new topics.

## Concepts applied

- Object-Oriented Programming (classes, attributes, methods)
- Encapsulation with `@property` and setters
- Custom `__str__` and `__repr__` methods
- List comprehensions and generator expressions
- Error handling with `try/except`
- Package structure with `pyproject.toml`
- Editable local installation (`pip install -e .`)

## Project structure
inventory-manager/
├── src/
│   └── store/
│       ├── init.py
│       ├── products.py
│       └── storage.py
├── tests/
│   └── test_products.py
├── main.py
├── pyproject.toml
└── README.md

## How to run

Clone the repository and set up a virtual environment:

```bash
git clone <repo-url>
cd inventory-manager

python3 -m venv venv
source venv/bin/activate

pip install -e .

python3 src/main.py
```

## Next steps

- Add automated tests (`pytest`)
- Add static typing checks (`mypy`)
- Improve input validation and error handling
- Explore persistence (saving/loading inventory data)