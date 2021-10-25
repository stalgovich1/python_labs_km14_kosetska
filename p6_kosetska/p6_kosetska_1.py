sentence1=(input('Введіть першу фразу: ')).lower()
sentence1=''.join(c for c in sentence1 if c.isalpha())
phrasentence1se1 = set (sentence1)
print(sentence1)
sentence2=(input('Введіть другу фразу: ')).lower()
sentence2=''.join(c for c in sentence2 if c.isalpha())
sentence2 = set (sentence2)
print(sentence2)
if sentence2 == sentence2 & sentence2:
    print ('Кожна з літер другої фрази зустрічається у першій')
else:
    print ('Не кожна з літер другої фрази зустрічається у першій')
