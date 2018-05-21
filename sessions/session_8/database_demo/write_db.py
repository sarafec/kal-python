import pymysql

f_name = input("Enter your first name")
l_name = input("Enter your last name")
age = int(input("Enter your age"))
gender = input("Enter your gender")
income = float(input("Enter your income: "))

sql = "INSERT INTO employees (First_Name, Last_Name, Age, Gender, Income)" \
    "VALUES('%s', '%s', '%d', '%s', '%d')" % (f_name, l_name, age, gender, income)

db = pymysql.connect("localhost", "root", "password", "employeeDb")
cursor = db.cursor()
cursor.execute(sql)
db.commit()

print("Employee added successfully.")