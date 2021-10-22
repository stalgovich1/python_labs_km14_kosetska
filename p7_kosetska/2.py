hex_numbers = '0123456789ABCDEF'
def hexadecimal(x):
    f=float(x)//16
    f=hex_numbers[int(f)]
    print(f,end = '')
    s=float(x)%16
    s=hex_numbers[int(s)]
    print(s, end = '')
def error(x):
    if x.isdigit():
        if 0 <= int(x) <= 255:
            return True
    print('Error')
    return False
while True:
    red=input('Enter red color level [0;255]: ')
    if error(red):
        break
while True:
    green=input('Enter green color level [0;255]: ')
    if error(green):
        break
while True:
    blue=input('Enter blue color level [0;255]: ')
    if error(blue):
        break
print('Hex color code: #',end = '')
for i in red,green,blue:
    hexadecimal(i)