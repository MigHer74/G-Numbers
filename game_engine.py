import db_functions as dba


def gEngine(gameType):
    allValues = []
    rowResult1 = []
    rowResult2 = []
    rowResult3 = []
    rowResult4 = []

    data = dba.dbaRetriveValues(gameType)

    for value in data:
        valueList = value[3:]
        for number in valueList:
            allValues.append(number)

    allValues.sort()

    if gameType == "short":
        for number in range(1, 40):
            choice = allValues.count(number)

            if choice >= 5:
                rowResult1.append(str(number))
            elif choice == 4:
                rowResult2.append(str(number))
            elif choice == 3:
                rowResult3.append(str(number))
            elif choice == 2:
                rowResult4.append(str(number))

            choice = 0
    else:
        for number in range(1, 57):
            choice = allValues.count(number)

            if choice >= 6:
                rowResult1.append(str(number))
            elif choice == 5:
                rowResult2.append(str(number))
            elif choice == 4:
                rowResult3.append(str(number))
            elif choice == 3:
                rowResult4.append(str(number))

            choice = 0

    return rowResult1, rowResult2, rowResult3, rowResult4
