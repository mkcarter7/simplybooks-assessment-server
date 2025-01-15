#SIMPLY BOOKS ASSESSMENT - BE README

#ABOUT
Simply Books is a Django web application for managing books and authors with user specific data.  Firebase is integrated for data management and authentication.

The user is able to manage their book inventory or lists.

#FEATURES
User Authentication is used for the user to be able to manage their own books
The user can manage book and author relationships showing a many to one relationship
The user can manage book and genre relationships are managed through a many-many  relationship
The user has full CRUD (create, read, update, delete operations) on books, authors and genre

#INSTALLATION
Basic Django Set Up
https://github.com/nashville-software-school/server-side-python-curriculum/blob/evening-cohorts/book-3-levelup/chapters/DRF_INSTALLS.md

#ERD

#VIDEO WALK THROUGH
https://www.loom.com/share/2ff029f2aa244e6ca6c585b8901e5792

#API DOCUMENTS
https://documenter.getpostman.com/view/33251382/2sAYQXpYXu

#TECH STACK
Django
Python
Postman
Firebase Auth


#BE DEFINITION OF DONE
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

#MVP Guidelines
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
#Submit:

Make sure to complete the README, Loom video demonstration, and submit your project with the deployed link.
