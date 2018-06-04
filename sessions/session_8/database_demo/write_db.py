import pymysql
from ReadConfig import read_db_config

db = None

try:
    f_name = input("Enter your first name")
    l_name = input("Enter your last name")
    age = int(input("Enter your age"))
    gender = input("Enter your gender")
    income = float(input("Enter your income: "))

    sql = "INSERT INTO employees (First_Name, Last_Name, Age, Gender, Income)" \
        "VALUES('%s', '%s', '%d', '%s', '%d')" % (f_name, l_name, age, gender, income)

    dbParam = read_db_config()
    db = pymysql.connect(**dbParam)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

    print("Employee added successfully.")
except ValueError:
    print("One of your inputs is invalid. Please try again.")
except Exception as err:
    print("Something went wrong: {0}".format(err))
else:
    print("in the finally block")
    if db != None:
        db.close()