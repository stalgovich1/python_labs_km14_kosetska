try:
    a=float(input('введіть квадратний коефіціент:'))
    b=float(input('введіть коефіціент біля x:'))
    c=float(input('введіть третій, вільнй член:'))
    D=(b**2-4*a*c)
except IndexError:
    print('a не може дорівнювати 0')
except IndexError:
    print('b не може дорівнювати 0!')
if(D < 0): raise Exception("discriminant is less than 0, there are no roots")
x1=(-b+D)/(2*a)
x2=(-b-D)/(2*a)
print("x1 =",x1,'x2 =',x2)