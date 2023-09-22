import sqlite3
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """CREATE TABLE School (
School_Id INTEGER NOT NULL PRIMARY KEY, 
School_Name TEXT NOT NULL, 
Place_Count INTEGER NOT NULL);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

sqlquery = """INSERT INTO School (School_Id, School_Name, Place_Count) 
VALUES 
('1', 'Протон', 200), 
('2', 'Преспектива', 300), 
('3', 'Спектр', 400), 
('4', 'Содружество', 500);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

sqlquery = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL PRIMARY KEY, 
Student_Name TEXT NOT NULL, 
School_Id INTEGER NOT NULL);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

sqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_Id) 
VALUES 
('201', 'Иван', 1), 
('202', 'Петр', 2), 
('203', 'Анастасия', 3), 
('204', 'Игорь', 4);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    con = get_connection()
    cursor = con.cursor()
    sqlquery = 'SELECT * FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE School.School_Id = ?'
    cursor.execute(sqlquery,(school_id,))
    student_info = cursor.fetchall()
    for row in student_info:
      print('ID студента:', row[0])
      print('Имя студента:', row[1])
      print('ID школы:', row[2])
      print('Название школы:', row[4],'\n')
    close_connection(con)
  except(Exception, sqlite3.Error) as error:
    print ('Ошибка вида', error)

get_school_name(2)