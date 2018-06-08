import pymysql
from read_config import read_db_config


def getEntryFromDb(id):
    db = None
    try:
        dbParam = read_db_config()
        db = pymysql.connect(**dbParam)
        cursor = db.cursor()

        sql = "SELECT * FROM Addresses WHERE id={0}".format(id)
        cursor.execute(sql)

        db.close()
        return cursor.fetchone()
    except ValueError:
        # print("One of your inputs is invalid. Please try again.")
        return ("error", "error", "error", "error", "error")
    except Exception as err:
        # print("Something went wrong: {0}".format(err))
        return ("error", "error", "error", "error", "error")
    else:
        if db != None:
            db.close()


def findLastId():
    db = None
    try:
        dbParam = read_db_config()
        db = pymysql.connect(**dbParam)
        cursor = db.cursor()

        sql = "SELECT * FROM Addresses ORDER BY id DESC LIMIT 1"
        cursor.execute(sql)

        idNum, targetName, targetStreet, targetCity, targetState, targetZip = cursor.fetchone()
        db.close()
        return idNum
    except ValueError:
        return 0
    except Exception as err:
        return 0
    else:
        if db != None:
            db.close()
