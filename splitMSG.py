'''
Author: Thoma4
Date: 2023-01-17 18:40:46
LastEditTime: 2023-01-18 00:24:39
Description: 
'''
import csv
import time as tm

tableHeader = ['Puzzle', 'Category', 'Time(millis)', 'Date(millis)',
               'Scramble', 'Penalty', 'Comment', 'dateTime']
# Backup_2023-01-17_17-52.txt
# cbmsg.csv
fPrefix = 'cblist'
fileType = '.csv'
resType, catagoryFliter, minT, maxT = '333', 'Normal', 9000, 60000  # 项目 组名
fSufix = ''
fileName = fPrefix + resType + fSufix + fileType

with open(file='cube/Backup_2023-01-17_17-52.txt', mode='r', encoding='utf-8') as rf:
    rlines = rf.readlines()
writerCSV = open(fileName, 'w', encoding='gb2312', newline='')
wf = csv.writer(writerCSV)
wf.writerow(tableHeader)

start_T = tm.time()
for line in rlines:
    row = line.split(';')
    for elem in range(0, len(row)):
        row[elem] = row[elem].strip('"\n')
    if len(row) > 6:  # 防止comment换行引起越界
        if row[6] != '':
            row[6] = ''  # 清除comment
        timeArray = tm.localtime(int(int(row[3]) / 1000))
        dateTime = tm.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        row.append(dateTime)
        if row[0] == resType\
                and row[1] == catagoryFliter\
                and minT < int(row[2]) < maxT:
            wf.writerow(row)
    # print(row)
writerCSV.close()
end_T = tm.time()
print('run_time: %0.3fs\n' % (end_T - start_T), end='')
