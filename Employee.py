import mysql.connector as db
x = db.connect(host="localhost",user="root",password="",database="Employee")
curs = x.cursor()
class Employee:
    def getdetails(self):
        self.id = input("Enter the Employee ID: ")
        self.name = input("Enter the Employee Name: ")
        self.mail = input("Enter the Employee email: ")
        self.password= input("Enter the Employee password: ")
    def insert(self):
        #curs.execute("CREATE TABLE EmployeeDetails1(id int, name VARCHAR(20), mail VARCHAR(40), password VARCHAR(15))")
        curs.execute("INSERT INTO EmployeeDetails1(id, name, mail, password) VALUES (%s, %s, %s, %s)", 
                     (self.id, self.name, self.mail, self.password))
        x.commit()
        print("Employee inserted successfully")
    def login(self):
        self.mail = input("Enter the Employee email: ")
        self.password = input("Enter the Employee password: ")
        curs.execute("SELECT * FROM EmployeeDetails1 WHERE mail = %s AND password = %s", (self.mail, self.password))
        record = curs.fetchall()
        if record:
            print("Login successful")
            print(record)
        else:
            print("Invalid credentials")
s=Employee()
s.getdetails()
s.insert()
s.login()
         
    

