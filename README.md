# MVC To-Do Application 📝

**Developers:** [Sergio](https://github.com/sergio-jorquera), [Hema](https://github.com/void-craft)

A colorful and interactive command-line task manager using the MVC (Model-View-Controller) architecture, built with Python and SQLAlchemy. This project was developed through pair programming, emphasizing clean code structure, collaboration, and real-world backend practices like database migrations and CI/CD.

![Screenshot 2025-05-26 222029](https://github.com/user-attachments/assets/c5122aed-96b9-4e63-88cf-8834ffe1a2e9)

## Features
✅ Create, view, update, and delete tasks
📅 Validated date input (DDMMYYYY format)
🎨 Color-coded interface:
  🟩 Green → Future tasks
  🟨 Yellow → Today's tasks
  🟥 Red → Overdue tasks
🗄️ Database versioning using Alembic
🧪 Automated testing with Pytest
🔄 CI/CD pipeline via GitHub Actions

## Stack
- Python
- PostgreSQL
- SQLAlchemy
- Alembic
- Pytest
- GitHub Actions
- MVC Pattern
  
## Quick Start
```bash
pip install -r requirements.txt # Install dependencies
alembic upgrade head # Apply latest DB migrations
python main.py # Launch the application
```

## Usage
- **Date format:** DDMMYYYY (e.g., 25122024)
- **Menu options:**
```
1-Create
2-View
3-Search
4-Update
5-Delete
6-Exit
```
## Testing
```bash
pytest                  # Run all tests
pytest -m create        # Creation tests only
pytest -v               # Verbose output
```

## Project Structure
```
├── .github/workflows
├── alembic/
│   ├── README.md
│   ├── env.py
├── controllers/task_controller.py    # Business logic
├── database/db.py                    # Database
├── models/task_model.py              # SQLAlchemy model
├── tests/                            # Test suite
│   ├── conftest.py
│   └── test_tasks.py
├── views/task_view.py                # View
├── main.py                           # Main interface
├── alembic.ini
├── pytest.ini
└── README.md
├── requirements.txt
```
## Test
The following tests ensure the reliability of key application functionalities:

### Test Cases
#### Unit Tests
- **TC-001:** Date validation
- **TC-002:** Task creation
- **TC-003-004:** Task retrieval
- **TC-005:** Task updates
- **TC-006:** Task deletion
- **TC-007:** Error handling
#### Integration Test
- **TC-008:** Full CRUD integration

## Collaboration
This project was developed through pair programming using Visual Studio Code Live Share, enabling real-time collaboration and agile workflow management. We split responsibilities based on MVC layers and alternated roles between driver and navigator.

Feel free to clone, fork, and contribute!
Happy coding!
