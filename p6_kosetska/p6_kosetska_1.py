phrase1=(input('Введіть першу фразу: ')).lower()
phrase1=''.join(c for c in phrase1 if c.isalpha())
phrase1 = set (phrase1)
print(phrase1)
phrase2=(input('Введіть другу фразу: ')).lower()
phrase2=''.join(c for c in phrase2 if c.isalpha())
phrase2 = set (phrase2)
print(phrase2)
if phrase2 == phrase1 & phrase2:
    print ('Кожна з літер другої фрази зустрічається у першій')
else:
    print ('Не кожна з літер другої фрази зустрічається у першій')