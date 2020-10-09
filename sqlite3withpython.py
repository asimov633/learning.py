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
while i<=5:
    name_sql=input("Name{}: ".format(i))
    surname_sql=input("Surname{}: ".format(i))
    age_sql=input("Age{}: ".format(i))
    lesson_sql=input("Lesson{}: ".format(i))

    appendtable()
    i=i+1

print("Table Append is done")
print("Do you wanna inside of table (yes/not)")
answer=input("Answer: ")

if answer.lower()=="yes":
    sql_cursor.execute("SELECT * FROM StudyPlan")
    data=sql_cursor.fetchall()
    print(data)
elif answer.lower()=="not":
    print("Cant see inside of table")

else:
    print("Pls Enter only (yes/not)")

