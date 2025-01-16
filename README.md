# Project Name: College Attendance Tracker

## Project Description
A web-based application to manage student attendance. Professors can log in, mark attendance, and view detailed monthly attendance reports. The system also allows adding or removing students from the database.

---

## Deliverables
1. Fully functional College Attendance Tracker web application.
2. Source code repository.
3. Database schema and SQLite database file.
4. User documentation for setup and usage.
5. Screenshots of the application.

---

## Screenshots
Below are screenshots demonstrating the key features of the project:

1. **Login Page**

   ![login png](https://github.com/user-attachments/assets/c14a938c-a0fe-45c1-9670-a562fa5c2c14)

   *Caption: Professors can log in to manage attendance.*

2. **Attendance Marking** 
 
   ![attendence](https://github.com/user-attachments/assets/ee649585-e8c6-481e-9463-2360f4eaafcb)

   *Caption: Mark students as present or absent for a specific day.*

3. **Attention MArking in Bulk **  

   ![bulk png](https://github.com/user-attachments/assets/e8fab768-a442-4df5-9933-e10da02f7669)
  
   *Caption: Mark students as present or absent for multiple day.*

4. **Monthly Attendance Report**  

   ![report png](https://github.com/user-attachments/assets/7378eb46-a51d-43aa-b2be-31f4b6c47296)
 
   *Caption: View monthly attendance for each student.*

---

## Technology Stack
The project was developed using the following technologies:

- **Framework:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Authentication:** Django Authentication System
- **Other Tools:** Git, Virtual Environment

---

## Steps to Run the Project

### Prerequisites
- Python 
- Django (latest version)
- Bootstrap (included in the html files)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository.git
   cd attendance_tracker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for accessing the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open the application in your browser at `http://127.0.0.1:8000`.

---

## Features
- Professor login system.
- Attendance tracking for students by date and division.
- Add/remove students from the database.
- View detailed monthly attendance reports.
- User-friendly interface with Bootstrap styling.

---

## Contact
For any questions or support, feel free to contact:
- **Name:** Rishi Ponda
- **Email:** rishiponda2004@gmail.com
- **Linkedin:** www.linkedin.com/in/rishi-ponda-625a30222
- **GitHub:** https://github.com/rishi0588

