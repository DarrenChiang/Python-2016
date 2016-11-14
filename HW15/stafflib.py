staffList = []

def addStaff(fN, lN, ag, vin, rol, dW, sal):
    """
    This function takes in multiple values and puts them in their respective slots inside a dictionary that holds all information of an employee. That dictionary is then added to a list, "staffList", that holds
    information for all employeeds.
    """
    temp = getTemplate()
    temp["firstName"] = fN
    temp["lastName"] = lN
    temp["age"] = ag
    temp["vinc"] = vin
    temp["role"] = rol
    temp["daysWorked"] = dW
    temp["salary"] = sal
    staffList.append(temp)

def returnStaff():
    """
    This function returns the list of all employees' information. It isn't used in this instance but is always useful.
    """
    return staffList

def showRegistre():
    """
    This function prints out the information of the employees in a specific format.
    """
     print("Showing registre of employees:")
     staffNumber = 1
     for i in staffList:
        string = "day"
        if i["daysWorked"] != 1:
            string += 's'
        print("Staff #" + str(staffNumber) + ": " + i["firstName"] + " " + i["lastName"] + " age " + str(i["age"]) + " has been working " + str(i["daysWorked"]) + " " + string + " since " + i["vinc"] + " as a " +  i["role"] + " for USD" + str(i["salary"]))
        staffNumber += 1

def addDay():
    """
    This function simulates the passing of a day by adding one to the "daysWorked" of every employee. Note: Their age and salary does not change with time.
    """
    for i in staffList:
        i["daysWorked"] += 1

def deleteStaff(fN, lN) :
    """
    This function takes the first name and last name to delete an employee.
    """
    for i in range(len(staffList)):
        if staffList[i]["firstName"] == fN:
            if staffList[i]["lastName"] == lN:
                del staffList[i]

def getTemplate():
    """
    This function is only for convenience.
    """
    return {"firstName": "", "lastName": "", "age": 0, "vinc": "", "role": "", "daysWorked": 0, "salary": 0}
