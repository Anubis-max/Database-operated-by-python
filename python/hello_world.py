import mysql.connector

try:
    connection = mysql.connector.connect(
        user='root', password='root', host='mysql', port="3306", database="db")
    print("DB connected")

    cursor = connection.cursor()

    add_student = "INSERT INTO students (FirstName, Surname) VALUES (%s, %s)"
    student_data = ("John", "Smith")

    cursor.execute(add_student, student_data)
    connection.commit()

    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()

    for student in students:
        print(student)

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
