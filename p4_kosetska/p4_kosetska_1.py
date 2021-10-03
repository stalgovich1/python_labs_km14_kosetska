user_name = input('Enter your name and surname: ')
number1 = input('Please enter a phone number ')
number2 = input('Please enter a street ')
number3 = input('Please enter a home number ')
number4 = input('Please enter a apartment number ')
number5 = input('Please enter a city ')
number6 = input('Please enter an index ')
number7 = input('Please enter a country ')
print('Hello,', user_name)
if number1.isdigit():
    print(number1)
else:
    print("Except numbers, there are other symbols!")
if number2.isalpha():
    print('str.', number2)
if number3.isdigit():
    print(number3)
else:
    print("Except numbers, there are other symbols!")
if number4.isdigit():
    print('ap.', number4)
else:
    print("Except numbers, there are other symbols!")
if number5.isalpha():
    print(number5)
else:
    print("Except letters, there are other symbols!")
if number6.isdigit():
    print(number6)
else:
    print("Except numbers, there are other symbols!")
if number7.isalpha():
     print(number7)
else:
     print("Except letters, there are other symbols!")
print('Thank you')
