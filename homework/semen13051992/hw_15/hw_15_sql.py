import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("insert into students (name, second_name) values ('Semen', 'Palchun')")
student_id = cursor.lastrowid

insert_books = f'insert into books (title, taken_by_student_id) values (%s, %s)'
cursor.executemany(
    insert_books, [
        ('python', student_id),
        ('sql', student_id)
    ]
)

cursor.execute("insert into `groups` (title, start_date, end_date) values ('Python Auto QA', 'jan 26', 'apr 26')")
groups_id = cursor.lastrowid

cursor.execute(f"update students set group_id = {groups_id} where id = {student_id}")

cursor.execute(f"insert into subjects (title) values ('python')")
subjects_id1 = cursor.lastrowid
cursor.execute(f"insert into subjects (title) values ('sql')")
subjects_id2 = cursor.lastrowid

cursor.execute(f"insert into lessons (title, subject_id) values ('python lesson1', {subjects_id1})")
python_lesson1 = cursor.lastrowid
cursor.execute(f"insert into lessons (title, subject_id) values ('python lesson2', {subjects_id1})")
python_lesson2 = cursor.lastrowid
cursor.execute(f"insert into lessons (title, subject_id) values ('sql lesson1', {subjects_id2})")
sql_lesson1 = cursor.lastrowid
cursor.execute(f"insert into lessons (title, subject_id) values ('sql lesson2', {subjects_id2})")
sql_lesson2 = cursor.lastrowid

insert_marks = "insert into marks (value, lesson_id, student_id) values (%s, %s, %s)"
cursor.executemany(
    insert_marks, [
        ('5', python_lesson1, student_id),
        ('7', python_lesson2, student_id),
        ('8', sql_lesson1, student_id),
        ('6', sql_lesson2, student_id),
    ]
)

db.commit()

cursor.execute(f"select value from marks where student_id = {student_id}")
print(cursor.fetchall())

cursor.execute(f"select title from books where taken_by_student_id = {student_id}")
print(cursor.fetchall())

cursor.execute("select s.name, s.second_name, b.title, g.title, g.start_date, g.end_date, m.value, l.title, sb.title"
               "from students s"
               "join books b on s.id = b.taken_by_student_id"
               "join `groups` g on s.group_id = g.id"
               "join marks m on s.id = m.student_id"
               "join lessons l on m.lesson_id = l.id"
               "join subjects sb on l.subject_id = sb.id"
               f"where s.id = {student_id}")
print(cursor.fetchall())

db.close()
