import csv
import re
with open('LanaDelRey.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Song','Year'])
    writer.writerow(['Summertime sadness',2012])
    writer.writerow(['F**k it I love you',2019])
    writer.writerow(['National Anthem',2012])
    writer.writerow(['Cola',2012])
    writer.writerow(['Blue Banisters',2021])
    writer.writerow(['Cherry',2017])
t=[]
with open('LanaDelRey.csv', 'r') as f:
    lines = f.readlines()
    print('The name of the file:',f.name)
    for line in lines:
        new_line = line.replace('\n', '')
        split = re.split(',',new_line)
        t.append(split)
        print(','.join(split))