# Event-Management-System

Event is a Task Management System built using **Django**, **Tailwind CSS**, and **HTML**.  
It features **Role-Based Access Control (RBAC)**, optimized database queries, and customized dashboards for different user roles (Admin, Manager, Employee).  
**Django Signals** are used to send email notifications for task assignments and user activation after registration.


---

## Features

- **Role-Based Access Control (RBAC)**
  - **Admin**: Full control of the system.
  - **Manager**: Can create, update, delete, and assign tasks.
  - **Employee**: Can view and complete assigned tasks.
- **Optimized Queries**: For better performance.
- **Customized Dashboard**: Different dashboards for Admin, Manager, and Employee.
- **Django Signals**:
  - Sends an email when a task is assigned.
  - Sends an activation email upon user registration.
- **User Authentication & Authorization**
- **Responsive UI**: Built with Tailwind CSS.
---

## Demo Credentials
| Role     | Username / Email      | Password          |
|----------|--------------------|-----------------|
| Admin    | admin              |     1234        |
| Manager  | manager            |     22334       |
| Employee | user               |     1357        |

---

## Installation

1. Clone the repository:

```bash
git clone <https://github.com/sujon-ahmed-WD/event_management_django>
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser (optional):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:

Open http://127.0.0.1:8000/ in your browser.

Technologies Used
Django - Backend framework

Tailwind CSS - Frontend styling

HTML - Templating

Django Signals - Email notifications

PostgreSQL/MySQL (Optional) - Database

Contributing
If you want to contribute, please submit a pull request.

License
This project is licensed under the MIT License.


Made with ❤️ by Md Sujon Ahmed