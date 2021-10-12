indices = {'Newfoundland': 'A',
         'Nova Scotia': 'B',
         'Prince Edward Island': 'C',
         'New Brunswick': 'E',
         'Quebec': ('G','H' , 'J'),
         'Ontario': ('K', 'L', 'M', 'N', 'P'),
         'Manitoba': 'R',
         'Saskatchewan': 'S',
         'Alberta': 'T',
         'British Columbia': 'V',
         'Nunavut': 'X',
         'Northwest Territories': 'X',
         'Yukon': 'Y' }
index = input("Enter the index: ".upper()).upper()
if index[0].isalpha() == False:
    print('ERROR')
    exit()
elif index[1].isdigit() == False:
    print('ERROR')
    exit()
elif index[2].isalpha() == False:
    print('ERROR')
    exit()
elif len(index) != 3:
    print('ERROR')
    exit()
n = ''
for i in indices.keys():
    if indices[i] == index[0]:
        n+= i 
if n == '':
    print('ERROR')
    exit()
print(("The name of the province: " + n).upper())
if index[1] == 0:
    print(('Village').upper())
else:
    print(('City').upper())