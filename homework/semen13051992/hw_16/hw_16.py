import mysql.connector as mysql
import os
import csv
import dotenv

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_csv = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

select_query = f'''
select *
from students s
join books b on s.id = b.taken_by_student_id
join `groups` g on s.group_id = g.id
join marks m on s.id = m.student_id
join lessons l on m.lesson_id = l.id
join subjects sb on l.subject_id = sb.id
'''
cursor.execute(select_query)
db_result = cursor.fetchall()

with open(eugene_file_csv, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    for row in file_data:
        if row not in db_result:
           print(row)

db.close()
