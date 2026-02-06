# FastResult Backend API

A comprehensive Django REST Framework backend for managing academic results, approvals, and institutional workflows in higher education institutions.

## Features

- **Multi-University Support**: Manage multiple universities with their own academic structures
- **Complete Academic Management**: Universities, Campuses, Faculties, Departments, Programs, Courses
- **Student Management**: Enrollment, course registration, status tracking
- **Lecturer Management**: Staff profiles, qualifications, course allocations
- **Exam Management**: Exam periods, calendars, rooms, invigilator assignments
- **Results Engine**: Result submission, grading, GPA calculation, CGPA tracking, transcript generation
- **Multi-Level Approvals**: Workflow-based approval system with multiple stages
- **Audit Logging**: Complete activity tracking and change logs
- **Notifications**: In-app notifications, announcements, and broadcasts
- **Reports**: Customizable reporting and analytics
- **JWT Authentication**: Secure token-based authentication
- **Role-Based Access Control**: Admin, Registrar, Department Head, Lecturer, Student, Clerk

## Project Structure

```
fastresult_backend/
├── backend/                    # Django project configuration
│   ├── settings/
│   │   ├── base.py           # Common settings
│   │   ├── dev.py            # Development settings
│   │   └── prod.py           # Production settings
│   ├── urls.py               # Main URL routing
│   ├── asgi.py               # ASGI configuration
│   └── wsgi.py               # WSGI configuration
├── core/                      # Shared utilities & base logic
│   ├── constants/            # Application-wide constants
│   ├── permissions/          # Custom permission classes
│   ├── mixins/               # Reusable model mixins
│   ├── pagination/           # Pagination classes
│   ├── validators/           # Validation functions
│   ├── utils/                # Utility functions
│   └── audit_helpers/        # Audit trail helpers
├── accounts/                 # Authentication & user management
├── universities/             # Multi-university support
├── academics/                # Academic structure (faculties, departments, programs, courses)
├── students/                 # Student profiles & enrollments
├── lecturers/                # Lecturer profiles & qualifications
├── exams/                    # Exam management
├── results/                  # Result management & GPA calculation
├── approvals/                # Multi-level approval workflows
├── audit/                    # Activity logging & auditing
├── notifications/            # Notifications & announcements
├── reports/                  # Reports & analytics
├── files/                    # File uploads & management
└── requirements/             # Python dependencies

```

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL 13+
- Redis (for caching and Celery)

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd fastresult_backend
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements/dev.txt
```

4. **Create .env file**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/accounts/token/` - Obtain JWT token
- `POST /api/accounts/token/refresh/` - Refresh JWT token
- `GET /api/accounts/profiles/me/` - Get current user profile

### Universities Management
- `GET/POST /api/universities/universities/` - University list/create
- `GET/POST /api/universities/campuses/` - Campus list/create
- `GET/POST /api/universities/academic-years/` - Academic year list/create
- `GET/POST /api/universities/semesters/` - Semester list/create
- `GET/POST /api/universities/grading-scales/` - Grading scale list/create
- `GET/POST /api/universities/credit-rules/` - Credit rules list/create

### Academics
- `GET/POST /api/academics/faculties/` - Faculty list/create
- `GET/POST /api/academics/departments/` - Department list/create
- `GET/POST /api/academics/programs/` - Program list/create
- `GET/POST /api/academics/courses/` - Course list/create
- `GET/POST /api/academics/course-allocations/` - Course allocation list/create

### Students
- `GET/POST /api/students/profiles/` - Student profile list/create
- `GET/POST /api/students/enrollments/` - Enrollment list/create
- `GET/POST /api/students/enrolled-courses/` - Enrolled courses list/create
- `GET/POST /api/students/documents/` - Student documents list/create
- `GET /api/students/profiles/{id}/enrollments/` - Get student enrollments

### Results
- `GET/POST /api/results/results/` - Results list/create
- `GET/POST /api/results/gpa-records/` - GPA records list/create
- `GET/POST /api/results/cgpa-records/` - CGPA records list/create
- `GET/POST /api/results/transcripts/` - Transcripts list/create
- `GET/POST /api/results/result-releases/` - Result releases list/create

### Approvals
- `GET/POST /api/approvals/submissions/` - Submissions list/create
- `GET/POST /api/approvals/approval-actions/` - Approval actions list/create
- `POST /api/approvals/approval-actions/{id}/approve/` - Approve submission
- `POST /api/approvals/approval-actions/{id}/reject/` - Reject submission
- `GET/POST /api/approvals/correction-requests/` - Correction requests list/create

### Exams
- `GET/POST /api/exams/exam-periods/` - Exam periods list/create
- `GET/POST /api/exams/exam-calendars/` - Exam calendars list/create
- `GET/POST /api/exams/exam-rooms/` - Exam rooms list/create
- `GET/POST /api/exams/invigilator-assignments/` - Invigilator assignments list/create

### Notifications
- `GET/POST /api/notifications/notifications/` - Notifications list/create
- `GET/POST /api/notifications/announcements/` - Announcements list/create
- `GET/POST /api/notifications/broadcasts/` - Broadcasts list/create

## Authentication

The API uses JWT (JSON Web Token) authentication. 

1. Obtain a token by sending credentials to `/api/accounts/token/`:
```bash
curl -X POST http://localhost:8000/api/accounts/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

2. Use the token in subsequent requests:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:8000/api/universities/universities/
```

## Database Models

### Core Models
- **UserProfile**: Extended user information with roles
- **University**: Main institution record
- **Campus**: University branch/location
- **AcademicYear**: Academic year (e.g., 2023/2024)
- **Semester**: Semester within an academic year

### Academic Models
- **Faculty**: Faculty/School within university
- **Department**: Department within faculty
- **Program**: Academic program/degree
- **Course**: Individual course/module
- **CourseAllocation**: Lecturer assignment to courses

### Student Models
- **StudentProfile**: Student information
- **StudentEnrollment**: Enrollment record
- **EnrolledCourse**: Individual course enrollment
- **StudentDocument**: Student documents (certificates, etc.)

### Lecturer Models
- **LecturerProfile**: Lecturer information
- **LecturerQualification**: Lecturer credentials

### Results Models
- **Result**: Main result record
- **ResultComponent**: Individual score components
- **Grade**: Calculated grade
- **GPARecord**: Semester GPA
- **CGPARecord**: Cumulative GPA
- **Transcript**: Student transcript
- **ResultLock**: Result modification lock
- **ResultRelease**: Result visibility control

### Approvals Models
- **Submission**: Result submission for approval
- **ApprovalStage**: Workflow stage definition
- **ApprovalAction**: Individual approval action
- **ApprovalHistory**: Approval change history
- **CorrectionRequest**: Correction request during approval

### Exam Models
- **ExamPeriod**: Exam period definition
- **ExamCalendar**: Individual exam schedule
- **ExamRoom**: Exam venue/room
- **InvigilatorAssignment**: Invigilator assignment

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/fastresult_db

# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email (for notifications)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# JWT
JWT_SECRET_KEY=your-jwt-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# Redis (for caching)
REDIS_URL=redis://localhost:6379/0

# AWS S3 (for file storage - optional)
USE_S3=False
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
```

### Django Settings

Settings are organized by environment:

- **base.py**: Common settings for all environments
- **dev.py**: Development-specific settings (DEBUG=True, local database)
- **prod.py**: Production-specific settings (DEBUG=False, security hardening)

### Running in Different Environments

```bash
# Development
python manage.py runserver --settings=backend.settings.dev

# Production
python manage.py runserver --settings=backend.settings.prod
```

## Testing

Run tests using pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific app tests
pytest tests/students/
```

## Migration Guide

Create and run migrations:

```bash
# Create migrations for model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

## Admin Interface

Access Django admin at `/admin/` with superuser credentials.

All models have been registered in the admin interface for easy management:
- Universities, Campuses, Academic Years, Semesters
- Faculties, Departments, Programs, Courses
- Student Profiles, Enrollments
- Lecturer Profiles
- Exams, Invigilators
- Results, Grades, GPA/CGPA Records
- Submissions, Approvals, Corrections
- Notifications, Announcements

## Performance Optimization

- Database indexing on frequently queried fields
- Pagination for large result sets
- Caching with Redis for frequently accessed data
- Selective field retrieval in serializers

## Security Features

- JWT token-based authentication
- Role-based access control (RBAC)
- Permission-level validation on all endpoints
- Input validation and sanitization
- CORS configuration
- CSRF protection
- SQL injection prevention (via ORM)
- Rate limiting (recommended for production)

## Deployment

### Docker Deployment

```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements/prod.txt .
RUN pip install -r prod.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
```

### Heroku Deployment

```bash
heroku create your-app-name
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key
git push heroku main
```

## API Documentation

Swagger/OpenAPI documentation can be generated using `drf-spectacular`:

```bash
pip install drf-spectacular
# Access at /api/schema/swagger-ui/
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## Support

For issues and questions, please contact the development team or create an issue in the repository.

## License

This project is licensed under the MIT License.
