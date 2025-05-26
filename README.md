# To-Do Application 📝

**Developers:** Sergio, Hema

A colorful command-line task manager built with Python, SQLAlchemy, and Alembic for database migrations.

## Features
- ✅ Create, view, update, and delete tasks
- 📅 Date management with validation
- 🎨 Color-coded interface (Green: future, Yellow: today, Red: overdue)
- 🗄️ Database migrations with Alembic
- 🧪 Complete test suite with pytest

## Quick Start
```bash
pip install -r requirements.txt
alembic upgrade head
python main.py
```

## Usage
- **Date format:** DDMMYYYY (e.g., 25122024)
- **Menu options:** 1-Create, 2-View, 3-Search, 4-Update, 5-Delete, 6-Exit

## Testing
```bash
pytest                    # Run all tests
pytest -m create         # Creation tests only
pytest -v               # Verbose output
```

## Project Structure
```
├── controllers/task_controller.py    # Business logic
├── database/db.py                    # Database
├── models/task_model.py              # SQLAlchemy model
├── alembic/                          # Database migrations
├── tests/                            # Test suite
│   ├── conftest.py
│   └── test_tasks.py
├── views/task_view.py                # View
└── main.py                           # Main interface
└── alembic.ini
└── pytest.ini
└── README.md
└── requirements.txt
```

## Test Cases
- **TC-001:** Date validation
- **TC-002:** Task creation
- **TC-003-004:** Task retrieval
- **TC-005:** Task updates
- **TC-006:** Task deletion
- **TC-007:** Error handling
- **TC-008:** Full CRUD integration
