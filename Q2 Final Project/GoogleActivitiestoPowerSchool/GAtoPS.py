import csv
import datetime

def getData(filename):
"""
Opens specified csv file and puts information in a list.
"""
    file = open(filename)
    fdata = csv.reader(file)
    content = [row for row in fdata]
    file.close()
    return content

def numFormat(num):
"""
Formats the score to limit to one decimal and round appropriately.
"""
    if num - int(num) != 0:
        if int(str(num)[3]) >= 5:
            num += (10 - int(str(num)[3])) * 10 ** -2
        else:
            num -= int(str(num)[3]) * 10 ** -2
    if num - int(num) != 0:
        return str(num)[0 : 3]
    else:
        return str(int(num))

def dateFormat(date):
"""
Takes the date format from Google Activities and converts into Powerschool format.
"""
    month = {'Jan': 1, 'Feb': 2, 'March': 3, 'Apr': 4, 'May': 5, 'June': 6,
             'July': 7, 'Aug': 8, 'Sept': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    dmy = date.split('-')
    dmy[2] = '20' + dmy[2]
    w = week[datetime.date(int(dmy[2]), int(month[dmy[1]]), int(dmy[0])).weekday()]
    if len(dmy[0]) < 2:
        dmy[0] = '0' + dmy[0]
    return w + ' ' + dmy[1] + ' ' + dmy[0] + ' 00:00:00 CST ' + dmy[2]

def studList(data, tdata):
"""
Creates the list of students in both Powerschool and Google Activity and ensures the proper placement of the student ID's.
"""
    studList = []
    for row in range(3, len(data)):
        dataName = data[row][1] + ', ' + data[row][0]
        for r2 in range(9, len(tdata)):
            if dataName.lower() == tdata[r2][1].lower():
                studList.append([tdata[r2][1], tdata[r2][0]])
    return studList           

data = getData('GoogleActivities.csv')
tdata = getData('PowerSchool Template.csv')

for i in range(3, len(data[0])):
    nFile = open('file' + str(i - 2) + '.csv', 'w', newline = '')
    writer = csv.writer(nFile, delimiter = ',')
    writer.writerow(['Teacher Name:', tdata[0][1]])
    writer.writerow(['Section:', 'Python'])
    writer.writerow(['Assignment Name:', data[0][i]])
    writer.writerow(['Due Date:', dateFormat(data[1][i])])
    writer.writerow(['Points Possible:', 10])
    writer.writerow(['Extra Points:', 0])
    writer.writerow(['Score Type:', 'Points'])
    writer.writerow('')
    writer.writerow(['Student ID', 'Student Name', 'Points'])
    stl = studList(data, tdata)
    for n in range(3, len(data)):
        dataName = data[n][1] + ', ' + data[n][0]
        for x in range(len(stl)):
            if dataName.lower() == stl[x][0].lower():
                writer.writerow([stl[x][1] , stl[x][0], numFormat(float(data[n][i]) * 10 / float(data[2][i]))])
    nFile.close()
    

