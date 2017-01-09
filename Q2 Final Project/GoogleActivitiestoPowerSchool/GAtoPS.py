import csv

gcFile = open('GoogleActivities.csv')
gcData = csv.reader(gcFile)

data = []

for i, row in enumerate(gcData):
    print('{}- '.format(i + 1), row)
    data.append(row)
    
gcFile.close()

nact = len(data[0]) - 3

for i, col in enumerate(data[0]):
    if i > 2:
        print('Act-{} : {}'.format(i - 2, col))

names = []
for i, row in enumerate(data):
    if i > 2:
        names.append(row[1] + ','+ row[0])
        print('Stu-{}: {}, {}'.format(i - 2, row[1], row[0]))

psFile = open('PowerSchool Template.csv')
psData = csv.reader(psFile)

tdata = []

for i, row in enumerate(psData):
    tdata.append(row)

psFile.close()
