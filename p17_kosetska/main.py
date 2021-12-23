from exp_root.exponentation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import factorial
from logarithm.logarithm import log, ln, lg


def main():
    chose = input('Choose function (1 for exponentiation; 2 for logarithmic; 3 for factorial; 4 for root):')
    if chose == '1':
        while True:
            n = input('Please, input exponentiation:')
            try:
                n = int(n)
                print('exp2:' + str(exp2(n)))
                print('exp3:' + str(exp3(n)))
                break
            except Exception:
                print('Uncorrect data!')
            else:
                raise Exception
                break
    elif chose == '2':
        while True:
            n1 = input('Please, input which type of logarithm you would like to chose (1 for log; 2 for ln; 3 for lg):')
            try:
                if n1 == '1':
                    a = int(input('Please, input a:'))
                    b = int(input('Please, input b:'))
                if a < 0 and b < 0:
                    raise Exception
                if a == 1 and b == 1:
                    raise Exception
                elif print('Log is:' + str(log(b, a))):
                    break
            except Exception as zer:
                print(zer)
            try:
                if n1 == '2':
                    a = int(input('Please, input a:'))
                if a<0:
                    raise Exception
                elif print('Ln is:' + str(log(a))):
                    break
            except Exception as s:
                print(s)
                try:
                    if n1 == '3':
                        a = int(input('Please, input a:'))
                    if a < 0:
                        raise Exception
                    elif print('Lg is:' + str(lg(a))):
                        break
                except Exception as k:
                    print(k)
    elif chose == '3':
        while True:
            f = input('Please, input factorial:')
            try:
                f = int(f)
                if f < 0:
                    raise Exception
                print('factorial:' + str(factorial(f)))
                break
            except Exception as m:
                print(m)
    elif chose == '4':
        while True:

            try:
                r = int(input('Please, input number:'))
                if r < 0:
                    raise Exception
                print('root2:' + str(root2(r)))
                print('root3:' + str(root3(r)))
                break
            except Exception as h:
                print(h)
            else:
                break






if __name__ == '__main__':
    main()