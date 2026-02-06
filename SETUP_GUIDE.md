# FastResult Backend - Setup Guide

## Quick Start Guide

### 1. Prerequisites
- Python 3.10 or higher
- PostgreSQL 13 or higher
- Redis (optional, for caching)
- pip or conda package manager

### 2. Installation Steps

#### Step 1: Clone and Setup Environment
```bash
# Clone repository
git clone <repository-url>
cd fastresult_backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

#### Step 2: Install Dependencies
```bash
# Install development dependencies
pip install -r requirements/dev.txt

# Or for production
pip install -r requirements/prod.txt
```

#### Step 3: Configure Environment Variables
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your configuration
# Update database credentials, email settings, etc.
```

#### Step 4: Database Setup
```bash
# Create PostgreSQL database
createdb fastresult_db

# Run migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

#### Step 5: Load Initial Data (Optional)
```bash
# Create test data
python manage.py shell < scripts/load_initial_data.py
```

#### Step 6: Run Development Server
```bash
python manage.py runserver
```

Server will be available at: http://localhost:8000

### 3. Access Points

- **Admin Panel**: http://localhost:8000/admin/
- **API Root**: http://localhost:8000/api/
- **API Docs** (if using drf-spectacular): http://localhost:8000/api/schema/swagger-ui/

### 4. First Time Setup Checklist

- [ ] Database configured and migrations applied
- [ ] Superuser created
- [ ] Environment variables configured
- [ ] Development server running
- [ ] Can access admin panel
- [ ] JWT token can be obtained

### 5. Create Initial Data

Login to admin and create:
1. **University**: Main institution
2. **Campus**: University location
3. **Faculty**: Academic division
4. **Department**: Department under faculty
5. **Program**: Degree/diploma program
6. **Courses**: Individual courses
7. **Academic Year**: e.g., 2023/2024
8. **Semester**: Semester within academic year

### 6. Common Commands

```bash
# Run development server with specific settings
python manage.py runserver --settings=backend.settings.dev

# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run tests
pytest

# Run tests with coverage
pytest --cov=.

# Create Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Clear database and start fresh
python manage.py flush
```

### 7. Testing API with cURL

#### Get Authentication Token
```bash
curl -X POST http://localhost:8000/api/accounts/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

Response will contain access and refresh tokens.

#### Use Token in Requests
```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  http://localhost:8000/api/universities/universities/
```

### 8. Database Backup and Restore

#### Backup
```bash
pg_dump fastresult_db > backup.sql
```

#### Restore
```bash
psql fastresult_db < backup.sql
```

### 9. Docker Setup (Optional)

```bash
# Build Docker image
docker build -t fastresult-backend .

# Run container
docker run -p 8000:8000 fastresult-backend
```

### 10. Troubleshooting

**Issue**: Database connection error
- Solution: Ensure PostgreSQL is running and credentials in .env are correct

**Issue**: Migration conflicts
- Solution: Run `python manage.py migrate --fake-initial` or reset migrations

**Issue**: Static files not loading
- Solution: Run `python manage.py collectstatic --no-input`

**Issue**: CORS errors in frontend
- Solution: Check CORS_ALLOWED_ORIGINS in settings

### 11. Production Deployment

For production deployment:
1. Set DEBUG=False
2. Update ALLOWED_HOSTS
3. Use strong SECRET_KEY
4. Configure proper database
5. Use environment-specific settings
6. Set up SSL/HTTPS
7. Use gunicorn or similar WSGI server
8. Configure nginx as reverse proxy
9. Set up proper logging
10. Enable security headers

### 12. Support

For issues or questions:
1. Check Django documentation: https://docs.djangoproject.com/
2. Check DRF documentation: https://www.django-rest-framework.org/
3. Create an issue in the repository

### 13. Next Steps

- Explore API endpoints
- Read API documentation
- Set up frontend integration
- Configure email notifications
- Setup automated tests
- Deploy to staging/production

---

**Last Updated**: February 2026
**Backend Version**: 1.0.0
