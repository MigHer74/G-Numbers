import db_functions as dba


def gEngine(gameType):
    allValues = []

    data = dba.dbaRetriveValues(gameType)

    for value in data:
        valueList = value[3:]
        for number in valueList:
            allValues.append(number)

    allValues.sort()

    print(allValues)


gEngine("long")
