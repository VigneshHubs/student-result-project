from db import connect_db

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            marks INT
        )
    """)
    conn.commit()
    conn.close()

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, marks) VALUES (%s, %s)", (name, marks))
    conn.commit()
    conn.close()
    print("Student added successfully")

def view_students():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

def main():
    create_table()
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
