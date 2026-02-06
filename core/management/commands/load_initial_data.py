"""
Management command to load initial/demo data
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from universities.models import University, Campus, AcademicYear, Semester, GradingScale, GradePoint, CreditRules
from academics.models import Faculty, Department, Program, Course
from accounts.models import UserProfile
from core.constants import UserRole, Semester as SemesterChoice
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Load initial data for FastResult application'

    def handle(self, *args, **options):
        self.stdout.write('Starting data loading...')
        
        # Create Universities
        self.stdout.write('Creating universities...')
        uni1, created = University.objects.get_or_create(
            code='UNI001',
            defaults={
                'name': 'Example University',
                'abbreviation': 'EU',
                'country': 'Country Name',
                'city': 'City Name',
                'website': 'https://example.edu',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created university: {uni1.name}'))
        
        # Create Campus
        self.stdout.write('Creating campuses...')
        campus, created = Campus.objects.get_or_create(
            code='MAIN',
            university=uni1,
            defaults={
                'name': 'Main Campus',
                'location': 'Downtown',
                'is_main': True,
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created campus: {campus.name}'))
        
        # Create Academic Year
        self.stdout.write('Creating academic years...')
        current_year = date.today().year
        academic_year, created = AcademicYear.objects.get_or_create(
            year=f'{current_year}/{current_year+1}',
            university=uni1,
            defaults={
                'start_date': date(current_year, 9, 1),
                'end_date': date(current_year+1, 6, 30),
                'is_current': True,
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created academic year: {academic_year.year}'))
        
        # Create Semesters
        self.stdout.write('Creating semesters...')
        sem1, created = Semester.objects.get_or_create(
            academic_year=academic_year,
            number=1,
            defaults={
                'name': 'First Semester',
                'start_date': date(current_year, 9, 1),
                'end_date': date(current_year, 12, 15),
                'registration_start': date(current_year, 8, 15),
                'registration_end': date(current_year, 9, 7),
                'exam_start': date(current_year, 12, 10),
                'exam_end': date(current_year, 12, 20),
                'is_current': True,
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created semester: {sem1.name}'))
        
        # Create Grading Scale
        self.stdout.write('Creating grading scales...')
        grading_scale, created = GradingScale.objects.get_or_create(
            name='Standard 4.0 Scale',
            university=uni1,
            scale_type='letter',
            defaults={
                'description': 'Standard grading scale from A to F',
                'min_score': 0,
                'max_score': 100,
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created grading scale: {grading_scale.name}'))
            
            # Create Grade Points
            grades = [
                ('A', 90, 100, 4.0),
                ('A-', 85, 89, 3.7),
                ('B+', 80, 84, 3.3),
                ('B', 75, 79, 3.0),
                ('B-', 70, 74, 2.7),
                ('C+', 65, 69, 2.3),
                ('C', 60, 64, 2.0),
                ('D', 50, 59, 1.0),
                ('F', 0, 49, 0.0),
            ]
            for grade, min_s, max_s, points in grades:
                GradePoint.objects.get_or_create(
                    grading_scale=grading_scale,
                    grade=grade,
                    defaults={
                        'min_score': min_s,
                        'max_score': max_s,
                        'point_value': points
                    }
                )
            self.stdout.write(self.style.SUCCESS('Created grade points'))
        
        # Create Credit Rules
        self.stdout.write('Creating credit rules...')
        CreditRules.objects.get_or_create(
            name='Standard',
            university=uni1,
            defaults={
                'minimum_credits_per_semester': 12,
                'maximum_credits_per_semester': 21,
                'minimum_gpa_for_graduation': 2.0,
                'minimum_gpa_for_good_standing': 2.0,
                'pass_grade': 'D'
            }
        )
        self.stdout.write(self.style.SUCCESS('Created credit rules'))
        
        # Create Faculty
        self.stdout.write('Creating faculties...')
        faculty, created = Faculty.objects.get_or_create(
            code='FCIT',
            university=uni1,
            defaults={
                'name': 'Faculty of Computing & IT',
                'description': 'Computing and Information Technology',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created faculty: {faculty.name}'))
        
        # Create Department
        self.stdout.write('Creating departments...')
        dept, created = Department.objects.get_or_create(
            code='CS',
            faculty=faculty,
            defaults={
                'name': 'Computer Science',
                'description': 'Computer Science Department',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created department: {dept.name}'))
        
        # Create Program
        self.stdout.write('Creating programs...')
        program, created = Program.objects.get_or_create(
            code='BSCS',
            department=dept,
            defaults={
                'name': 'Bachelor of Science in Computer Science',
                'level': 'bachelors',
                'duration_years': 4,
                'total_credits': 120,
                'description': 'A 4-year undergraduate program',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created program: {program.name}'))
        
        # Create Courses
        self.stdout.write('Creating courses...')
        courses_data = [
            ('CS101', 'Introduction to Programming', 3, 100),
            ('CS102', 'Data Structures', 3, 100),
            ('CS201', 'Database Systems', 4, 200),
            ('CS202', 'Web Development', 3, 200),
        ]
        for code, name, credits, level in courses_data:
            Course.objects.get_or_create(
                code=code,
                program=program,
                defaults={
                    'name': name,
                    'credit_units': credits,
                    'level': level,
                    'is_compulsory': True,
                    'is_active': True
                }
            )
        self.stdout.write(self.style.SUCCESS('Created courses'))
        
        # Create admin user
        self.stdout.write('Creating admin user...')
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.edu',
                'first_name': 'Admin',
                'last_name': 'User',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Created admin user'))
            
            # Create admin profile
            UserProfile.objects.get_or_create(
                user=admin_user,
                defaults={
                    'university': uni1,
                    'role': UserRole.ADMIN,
                    'is_verified': True
                }
            )
        
        self.stdout.write(self.style.SUCCESS('\n✅ Data loading completed successfully!'))
        self.stdout.write('\nYou can now login with:')
        self.stdout.write('Username: admin')
        self.stdout.write('Password: admin123')
