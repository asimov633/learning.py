import sqlite3
sql_connection=sqlite3.connect("StudyPlan.db")
sql_cursor=sql_connection.cursor()

def createtable():
    sql_cursor.execute("CREATE TABLE StudyPlan (name TEXT, surname TEXT, age TEXT,lesson TEXT)")

def appendtable():
    sql_cursor.execute("INSERT INTO StudyPlan (name,surname,age,lesson) VALUES (?,?,?,?)",(name_sql,surname_sql,age_sql,lesson_sql))
    sql_connection.commit()



createtable()
i=1
#Enter how much increase you want.(i)
while i<=4:
    name_sql=input("Name{}: ".format(i))
    surname_sql=input("Surname{}: ".format(i))
    age_sql=input("Age{}: ".format(i))
    lesson_sql=input("Lesson{}: ".format(i))

    appendtable()
    i=i+1

print("Table Append is done")

