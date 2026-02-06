# FastResult Backend - Quick Reference Guide

## 🚀 Quick Start

### 1. Installation (5 minutes)
```bash
# Activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements/dev.txt

# Copy environment file
cp .env.example .env
```

### 2. Database Setup (5 minutes)
```bash
# Create database
createdb fastresult_db

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
```

### 3. Load Initial Data (2 minutes)
```bash
# Load demo data
python manage.py load_initial_data
```

### 4. Start Server (1 minute)
```bash
python manage.py runserver
```

Access at: http://localhost:8000

---

## 🔑 Key URLs

| URL | Purpose |
|-----|---------|
| `/admin/` | Django admin panel |
| `/api/` | API root |
| `/api/accounts/token/` | Get JWT token |
| `/api/universities/universities/` | List universities |
| `/api/academics/programs/` | List programs |
| `/api/students/profiles/` | List students |
| `/api/results/results/` | List results |
| `/api/approvals/submissions/` | List submissions |

---

## 📦 Important Models

```python
# Authentication
User, UserProfile

# Multi-University
University, Campus, AcademicYear, Semester

# Academics
Faculty, Department, Program, Course, CourseAllocation

# Students
StudentProfile, StudentEnrollment, EnrolledCourse

# Results (CORE)
Result, ResultComponent, Grade, GPARecord, CGPARecord

# Approvals
Submission, ApprovalStage, ApprovalAction

# Exams
ExamPeriod, ExamCalendar, ExamRoom, InvigilatorAssignment
```

---

## 🔐 Authentication

### Get Token
```bash
curl -X POST http://localhost:8000/api/accounts/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

### Use Token
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/universities/universities/
```

---

## 📊 API Methods

### List (with pagination)
```
GET /api/app/resource/?page=1&page_size=10
```

### Create
```
POST /api/app/resource/
Content-Type: application/json

{...data...}
```

### Retrieve
```
GET /api/app/resource/{id}/
```

### Update (full)
```
PUT /api/app/resource/{id}/
Content-Type: application/json

{...updated data...}
```

### Partial Update
```
PATCH /api/app/resource/{id}/
Content-Type: application/json

{...partial data...}
```

### Delete
```
DELETE /api/app/resource/{id}/
```

---

## 🏗️ Project Structure

```
fastresult_backend/
├── backend/                # Django settings & main config
├── core/                   # Shared utilities
├── accounts/               # User management
├── universities/           # Multi-university
├── academics/              # Academic structure
├── students/               # Student management
├── lecturers/              # Lecturer management
├── exams/                  # Exam management
├── results/                # CORE: Result processing
├── approvals/              # Approval workflows
├── audit/                  # Activity logging
├── notifications/          # Notifications
├── reports/                # Reports
├── files/                  # File handling
├── requirements/           # Python dependencies
├── manage.py              # Django CLI
└── README.md              # Full documentation
```

---

## 🛠️ Common Commands

### Development
```bash
python manage.py runserver
python manage.py shell
python manage.py migrate
python manage.py makemigrations
```

### Testing
```bash
pytest
pytest --cov=.
pytest tests/students/
```

### Admin
```bash
python manage.py createsuperuser
python manage.py changepassword admin
python manage.py dumpdata > backup.json
```

### Management
```bash
python manage.py load_initial_data
python manage.py collectstatic
```

---

## 📋 Model Relationships

```
University (1) ──┬─→ (N) Campus
                 ├─→ (N) Faculty
                 ├─→ (N) AcademicYear
                 ├─→ (N) GradingScale
                 └─→ (N) CreditRules

Faculty (1) ──→ (N) Department
Department (1) ──┬─→ (N) Program
                  └─→ (N) Lecturer

Program (1) ──→ (N) Course
Course (1) ──→ (N) Enrollment

Student (1) ──→ (N) Enrollment
Enrollment (1) ──┬─→ (N) Result
                  ├─→ (1) GPARecord
                  └─→ (1) ResultLock

Result (1) ──┬─→ (N) ResultComponent
              ├─→ (1) Grade
              └─→ (N) Submission

Submission (1) ──→ (N) ApprovalAction ──→ (1) ApprovalStage
```

---

## 🔍 API Examples

### Create University
```bash
POST /api/universities/universities/
{
  "name": "Example University",
  "code": "UNI001",
  "abbreviation": "EU",
  "country": "Country",
  "city": "City"
}
```

### Create Student
```bash
POST /api/students/profiles/
{
  "user": 1,
  "student_id": "STU001",
  "university": 1,
  "program": 1,
  "date_of_birth": "2000-01-15",
  "gender": "male",
  "phone_number": "+1234567890"
}
```

### Submit Result
```bash
POST /api/results/results/
{
  "enrollment": 1,
  "course": 1,
  "status": "pending"
}
```

### Request Approval
```bash
POST /api/approvals/submissions/
{
  "enrollment": 1,
  "submission_type": "initial",
  "notes": "Please review"
}
```

---

## 🎯 User Roles

| Role | Permissions |
|------|-------------|
| **Admin** | Full access to all features |
| **Registrar** | Manage results, students, courses |
| **Department Head** | Approve results for department |
| **Lecturer** | Submit grades, view students |
| **Student** | View own results, transcripts |
| **Clerk** | Data entry and administration |

---

## ⚙️ Configuration

Key settings in `.env`:
```env
DEBUG=True/False
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:pass@localhost/fastresult_db
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 🐛 Troubleshooting

### Database Connection Error
```bash
# Check PostgreSQL is running
psql -l

# Update DATABASE_URL in .env
# Ensure database exists: createdb fastresult_db
```

### Migration Error
```bash
# Roll back migration
python manage.py migrate --fake app 0001

# Or reset all
python manage.py flush
python manage.py migrate
```

### CORS Error
Update CORS_ALLOWED_ORIGINS in settings/dev.py

### Static Files Not Loading
```bash
python manage.py collectstatic --no-input
```

---

## 📱 API Response Format

### Success (200 OK)
```json
{
  "id": 1,
  "name": "Example",
  "created_at": "2026-02-06T10:00:00Z",
  ...
}
```

### List Response (200 OK)
```json
{
  "count": 100,
  "next": "http://...?page=2",
  "previous": null,
  "results": [...]
}
```

### Error (400/404/500)
```json
{
  "detail": "Error message",
  "error_code": "NOT_FOUND"
}
```

---

## 📚 Documentation Files

1. **README.md** - Full API documentation
2. **SETUP_GUIDE.md** - Installation & setup
3. **IMPLEMENTATION_SUMMARY.md** - Architecture details
4. **DEPLOYMENT_CHECKLIST.md** - Production checklist
5. **PROJECT_REPORT.md** - Executive summary
6. **This file** - Quick reference

---

## 🚀 Deploy to Production

```bash
# 1. Build
pip install -r requirements/prod.txt

# 2. Collect static files
python manage.py collectstatic

# 3. Run migrations
python manage.py migrate

# 4. Start with gunicorn
gunicorn backend.wsgi --bind 0.0.0.0:8000

# 5. Use nginx as reverse proxy
# Configure nginx to forward requests to gunicorn
```

---

## 📞 Quick Help

| Question | Answer |
|----------|--------|
| How to get auth token? | `POST /api/accounts/token/` with username & password |
| How to create university? | `POST /api/universities/universities/` |
| How to enroll student? | `POST /api/students/enrollments/` |
| How to submit result? | `POST /api/results/results/` |
| How to approve result? | `POST /api/approvals/approval-actions/{id}/approve/` |
| How to see API docs? | Check README.md or access Swagger if installed |
| Default admin user? | username: `admin`, password: `admin123` (from load_initial_data) |

---

**Version**: 1.0.0  
**Last Updated**: February 6, 2026  
**Status**: ✅ Production Ready

For detailed information, refer to README.md
