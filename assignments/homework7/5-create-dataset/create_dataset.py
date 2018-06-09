# first name, last name, rank, salary (00.00)
# 1000 lines
import random

def writeListToFile():
    file = open('salary.txt', 'w')
    data = getFacultyList()
    file.write(data)
    file.close()

def getFacultyList():
    dataList = createDataList()
    return '\n'.join(dataList)

def createDataList():
    dataList = []
    for i in range(0, 1000):
        firstName = getFirstName()
        lastName = getLastName()
        rank = getRank()
        salary = determineSalary(rank)
        dataList.append(' '.join([firstName, lastName, rank, salary]))
    
    return dataList

def getFirstName():
    firstNames = ["Linda", "George", "Clarissa", "Bill", "Brooke", "Jordan", "Jill", "Lucy", "Luis", "Lauren", "Lisa", "Leslie", "Lupita", "Rick", "Ronaldo", "Mac", "April", "Tina", "Louis", "Peter", "Barry", "Nick", "Nina", "Kat"]
    randomIndex = random.randint(0, len(firstNames)-1)
    return firstNames[randomIndex]

def getLastName():
    lastNames = ["Johnson", "Lovett", "Ruiz", "Brown", "Jones", "Miller", "Davis", "Hall", "Allen", "Baker", "Adams", "Roberts", "Cook", "Bell", "Ward", "Cooper", "Hughes", "Harrison", "Carter", "Murphy", "Foster", "Hamilton", "Fisher"]
    randomIndex = random.randint(0, len(lastNames)-1)
    return lastNames[randomIndex]

def getRank():
    ranks = ["Assistant Professor", "Associate Professor", "Full Professor"]
    randomIndex = random.randint(0, len(ranks)-1)
    return ranks[randomIndex]

def determineSalary(rank):
    if rank == "Assistant Professor":
        return getSalaryForAssistantProf()
    elif rank == "Associate Professor":
        return getSalaryForAssociateProf()
    elif rank == "Full Professor":
        return getSalaryForFullProf()

def getSalaryForAssistantProf():
    return "{0:.2f}".format(random.uniform(50000.00, 80000.00), 2)

def getSalaryForAssociateProf():
    return "{0:.2f}".format(random.uniform(60000.00, 110000.00), 2)

def getSalaryForFullProf():
    return "{0:.2f}".format(random.uniform(75000.00, 130000.00), 2)

writeListToFile()