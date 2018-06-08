import pymysql
from read_config import read_db_config


def writeToDb(name, street, city, state, zip_code):
    db = None
    try:
        sql = "INSERT INTO Addresses (Full_Name, Full_Address, City_Name, State_Name, Zip_Code)" \
            "VALUES('%s', '%s', '%s', '%s', '%d')" % (name, street, city, state, zip_code)

        dbParam = read_db_config()
        db = pymysql.connect(**dbParam)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

        print("Address added successfully.")
    except ValueError:
        print("One of your inputs is invalid. Please try again.")
    except Exception as err:
        print("Something went wrong: {0}".format(err))
    else:
        if db != None:
            db.close()