import random as rdm
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

            rowFinal = final_values(rowResult1, rowResult2, rowResult3,
                                    rowResult4)
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

            rowFinal = final_values(rowResult1, rowResult2, rowResult3,
                                    rowResult4)

    return rowResult1, rowResult2, rowResult3, rowResult4, rowFinal


def final_values(row1, row2, row3, row4):
    final_list = []
    temp_list = []

    for row in [row1, row2, row3, row4]:
        if len(final_list) < 6:
            if len(row) != 0 and len(row) <= 6:
                for number in row:
                    if len(final_list) < 6:
                        final_list.append(number)
                    else:
                        break
            elif len(row) > 6:
                temp_list = row.copy()
                for item in range(6 - len(final_list)):
                    selection = rdm.choice(temp_list)
                    final_list.append(selection)
                    temp_list.remove(selection)

    return final_list
