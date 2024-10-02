from icecream import ic
from django.core.management.base import BaseCommand
from users.models import Teacher, Student, User, UserTypes
from courses.models import Course
from faker import Faker
from datetime import date, timedelta


class Command(BaseCommand):
    help = "Creates teachers, students, & courses non-interactively"

    

    def handle(self, *args, **options):
        try:
            fake = Faker()
            # teachers
            for i in range(3):
                f_name = fake.first_name()
                l_name = fake.last_name()
                email = f"{f_name.lower()}_{l_name.lower()}@teacher.university.com"
                
                _user = User.objects.create(
                    email = email,
                    username = email,
                    password= '1qweqwe23',
                    first_name = f_name,
                    last_name = l_name,
                    user_type = UserTypes.TEACHER,
                    is_verified = True
                )
                _teacher = Teacher.objects.create(
                    user = _user,
                    teacher_id = f'T00{i+1}'
                )
            # students
            for i in range(15):
                f_name = fake.first_name()
                l_name = fake.last_name()
                email = f"{f_name.lower()}_{l_name.lower()}@student.university.com"
                
                _user = User.objects.create(
                    email = email,
                    username = email,
                    password= '1qweqwe23',
                    first_name = f_name,
                    last_name = l_name,
                    user_type = UserTypes.STUDENT,
                    is_verified = True
                )
                _student = Student.objects.create(
                    user = _user,
                    registration = f'S00{i+1}',
                    name = f'{f_name} {l_name}'
                )
            
            # courses 
            _teachers = Teacher.objects.all()
            _students = Student.objects.all()
            _courses = ['Literature', 'Science', 'Business']
            for i, _course in enumerate(_courses):
                course = Course.objects.create(
                    name = _course,
                    teacher = _teachers[i],
                    exam_date = date.today()+ timedelta(days=i*2)
                )
                course.students.set(_students[i*5:5+i*5])

                
        except Exception as e:
            ic(e)