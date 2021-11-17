# ВАШ КОД ТУТ

def cons(head, tail = []):
    list = [head]
    for i in tail:
        list.append(i)
    return list

# ПЕРЕВІРКА

l = cons(3, 
        cons(2, 
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')

# ВАШ КОД ТУТ

def sum(n):
    if len(n)==0:
        return sum(n)+sum(n-1)

# ПЕРЕВІРКА

print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')