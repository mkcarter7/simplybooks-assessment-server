Simply Books Assessment - BE Readme

	About
Simply Books is a Django web application for managing books and authors with user specific data.  Firebase is integrated for data management and authentication.

The user is able to manage their book inventory or lists.

	Features
User Authentication is used for the user to be able to manage their own books
The user can manage book and author relationships showing a many to one relationship
The user can manage book and genre relationships are managed through a many-many  relationship
The user has full CRUD (create, read, update, delete operations) on books, authors and genre

	Installation
Basic Django set up
Or follow below:
pipenv shell # initialize a new virtual environment
django-admin startproject projectname
echo '[FORMAT] \n  good-names=i,j,ex,pk\n\n[MESSAGES CONTROL]\n  disable=broad-except,imported-auth-user,missing-class-docstring,no-self-use,abstract-method\n\n[MASTER]\n  disable=C0114,\n' > .pylintrc
Open VS Code and press ⌘SHIFTP (Mac), or CtrlSHIFTP (Windows) to open the Command Palette, and select "Python: Select Interpreter".
Find the option that has:
<YOUR_FOLDER_NAME>-<RANDOM_STRING>
Pylint Settings for Django
Add .vscode directory and add a settings.json with this info
{
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
        "--django-settings-module=<folder name>.settings",
    ],
}
python manage.py startapp projectnameapi
Uncomment out the Pipfile.lock line to make sure this gets ignored
Add .vscode to the .gitignore file.
Make the below changes to the settings.py file

# UPDATE THIS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'levelupapi',
]

# THIS IS NEW
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://127.0.0.1:3000'
)

# UPDATE THIS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
python manage.py migrate
Add the below to the .vscode/launch.json file
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver"],
            "django": true,
            "autoReload":{
                "enable": true
            }
        }
    ]
}
python manage.py runserver
Design models and make migrations
Create fixtures
You are ready to create views, models, urls, etc.
Happy Coding!

	ERD
![alt text](<Screenshot 2025-01-11 112810.png>)

	Video


	API Documents


	Tech Stack
Django
Python
Firebase

	BE Definition of Done
A feature or task is considered "done" when:

All tasks, features, and fixes must be ticketed and included on the GitHub project board. Make sure the project board uses columns like Backlog, In Progress, Testing, and Done to track work.
The code is fully implemented and meets the requirements defined in the task.
The feature passes all AC especially for CRUD functionality.
The user can successfully perform Create, Read, Update, and Delete operations for both books and authors using postman.
All relationships between authors and books are correctly established and maintained.
The API docs are deployed on Postman, and all features work in the deployed environment.
The README is updated with any relevant instructions, and a Loom video (max 5 minutes) demonstrates the app's features.
For any stretch goals, the feature must be functional and demonstrate proper user interaction (e.g., public/private book functionality, simulated purchase).
Any issues or bugs identified during development or testing must be fixed by the developer. All work related to fixes must be ticketed and included on the GitHub project board.
The project board must reflect all tasks, bugs, and updates, with each task being moved through the proper columns (Backlog, In Progress, Testing, Done).
MVP Guidelines
The Minimum Viable Product (MVP) for the Simply Books project includes:

CRUD Functionality for Books and Authors:

Users must be able to create, read, update, and delete books and authors.
When viewing an author, all books associated with that author must be visible.
When deleting an author, all of their books are also deleted.
Author-Book Relationship:

Each book must be associated with an author.
When a user views a book, the associated author's details must be accessible.
Firebase Integration:

The app must use Firebase for authentication and real-time data management.
Books and authors are tied to the logged-in user.
User-Specific Data:

Each user should only see their own books and authors.
Stretch Goals:
Public/Private Books:

Users can mark books as public or private.
Public books are viewable by all users without needing to log in.
Private books are only visible to the user who created them.
Simulated Book Purchases:

Users can add books to a cart and simulate purchasing them.
No real transaction will occur, but the UI will allow users to add items to the cart and check out.
Guide to Getting Started
Follow the deployment guide to get your app live!

Follow the Guide:

Detailed steps for each part of the project can be found in the Guide to getting started with this project.
Submit:

Make sure to complete the README, Loom video demonstration, and submit your project with the deployed link.
