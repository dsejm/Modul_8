import sqlite3

conn = sqlite3.connect('db1.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Students (id INTEGER PRIMARY KEY, name Varchar(32), surname Varchar(32), age int, city Varchar(32))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (id INTEGER PRIMARY KEY, name Varchar(32), time_start Varchar(32), time_end Varchar(32))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Student_courses (student_id int, courses_id int, FOREIGN KEY(student_id) REFERENCES Students(id), FOREIGN KEY(courses_id) REFERENCES Courses(id))''')

cursor.executemany('''INSERT OR IGNORE INTO Students VALUES (?, ?, ?, ?, ?)''', [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')])
cursor.executemany('''INSERT OR IGNORE INTO Courses VALUES (?, ?, ?, ?)''', [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')])
cursor.executemany('''INSERT OR IGNORE INTO Student_courses VALUES (?, ?)''', [(1, 1), (2, 1), (3, 1), (4, 2)])
conn.commit()

students_30_old = cursor.execute('SELECT name FROM Students WHERE age > 30').fetchall()
print(students_30_old)
python_curses_students = cursor.execute('''SELECT Students.name
                                        FROM Students, Courses, Student_courses
                                        WHERE (Courses.id = 1) AND (Student_courses.courses_id = Courses.id) AND (Students.id = Student_courses.student_id)''').fetchall()
print(python_curses_students)
python_students_spb = cursor.execute('''SELECT Students.name
                                        FROM Students, Courses, Student_courses
                                        WHERE (Courses.id = 1) AND (Student_courses.courses_id = Courses.id) AND (Students.id = Student_courses.student_id) AND (Students.city = 'Spb')''').fetchall()
print(python_students_spb)
# cursor.execute('SELECT * FROM Students')
# print(cursor.fetchall())
# cursor.execute('SELECT * FROM Courses')
# print(cursor.fetchall())
# cursor.execute('SELECT * FROM Student_courses')
# print(cursor.fetchall())

conn.close()
