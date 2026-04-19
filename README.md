# Task Manager API

This is a simple backend API I built using FastAPI.  
It allows users to create, view, update, and delete tasks.

The goal of this project was to understand how APIs work, how to connect to a database, and how to structure a backend project properly.


## What the API can do

- Add a new task
- View all tasks
- View a single task using its ID
- Update a task
- Delete a task



## Tech used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn



## How to run the project

1. Clone the repository
git clone https://github.com/your-username/task-manager-api.git

cd task-manager-api


2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Create a .env file and add:
DATABASE_URL=sqlite:///./tasks.db

5. Start the server
uvicorn app.main:app --reload



## API Endpoints

- POST /tasks → create a task  
- GET /tasks → get all tasks  
- GET /tasks/{id} → get one task  
- PUT /tasks/{id} → update a task  
- DELETE /tasks/{id} → delete a task  



## Testing the API

After running the server, go to:

http://127.0.0.1:8000/docs

You can test all the endpoints from there.



## What I learned

- How to build a REST API using FastAPI  
- How to connect Python to a database using SQLAlchemy  
- How CRUD operations work in real applications  
- How to structure a backend project  



## Author

Hasiyatu Ismail