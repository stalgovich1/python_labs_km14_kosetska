f = open('gadsby.txt')
text = f.read()
h = [x.lower() for x in text if 96<ord(x)<123 or 64<ord(x)<91]
a = 'abcdefghijklmnopqrstuvwxyz'
m=[]
d1 = {
}
for u in a:
    m.append(h.count(u)/len(text))
    d1[u] = 100*h.count(u)/len(h)
list_d = list(d1.items())
list_d.sort(key=lambda i: i[1])
t=[]
for i in list_d:
    t.insert(0,str(i[0])+ ':'+ str(i[1]))
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t[-5])
print(t[-4])
print(t[-3])
print(t[-2])
print(t[-1])