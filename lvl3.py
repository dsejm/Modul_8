from peewee import *
conn = SqliteDatabase("db2.sqlite")
cursor = conn.cursor()
class Students(Model):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')
    class Meta:
        database = conn
class Courses(Model):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    time_start = CharField(column_name='time_start')
    time_end = CharField(column_name='time_end')
    class Meta:
        database = conn

class Student_courses(Model):
    student_id = ForeignKeyField(Students, to_field='id',  column_name='student_id')
    courses_id = ForeignKeyField(Courses, to_field='id', column_name='courses_id')
    class Meta:
        database = conn


def create_tbls():
    Students.create_table()
    Courses.create_table()
    Student_courses.create_table()

def insert_coluns():
    student = Students(name="Max", surname="Brooks", age=24, city="Spb")
    student.save()
    student = Students(name="John", surname="Stones", age=15, city="Spb")
    student.save()
    student = Students(name="Andy", surname="Wings", age=45, city="Manchester")
    student.save()
    student = Students(name="Kate", surname="Brooks", age=34, city="Spb")
    student.save()

    courses = Courses(name="python", time_start="21.07.2021", time_end="21.08.2021")
    courses.save()
    courses = Courses(name="java", time_start="13.07.2021", time_end="16.08.2021")
    courses.save()

    student_course = Student_courses(student_id=1, courses_id=1)
    student_course.save()
    student_course = Student_courses(student_id=2, courses_id=1)
    student_course.save()
    student_course = Student_courses(student_id=3, courses_id=1)
    student_course.save()
    student_course = Student_courses(student_id=4, courses_id=2)
    student_course.save()

create_tbls()
insert_coluns() # После создания и заполнения таблиц вызов функций следует закомментировать


students_30_old = Students.select().where(Students.age > 30)
for i in students_30_old:
    print(i.name)
print('\n')

python_curses_students = Students.select().join(Student_courses).join(Courses).where(Courses.name == 'python')
for i in python_curses_students:
    print(i.name)
print('\n')

python_students_spb = Students.select().join(Student_courses).where(Student_courses.courses_id == 1, Students.city == 'Spb')
for i in python_students_spb:
    print(i.name)

conn.close()
