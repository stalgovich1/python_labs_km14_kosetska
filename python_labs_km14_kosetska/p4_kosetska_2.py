speed = float(input("Enter what is the wind speed: "))
if (speed > 0) and (speed < 137):
    print("Minor")
elif (speed > 137) and (speed < 177):
    print('Moderate')
elif (speed > 177) and (speed < 217):
    print('Considerable')
elif (speed > 217) and (speed < 266):
    print('Severe')
elif (speed > 266) and (speed < 322):
    print('Devastating')
elif speed > 322:
    print('Incredible')
elif speed < 0:
    print('Sorry, mistake!')
else:
    print('Thank you')