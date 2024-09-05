sp = [4, "Hello", 7.54, True, 1]

sp.append("World") # добавление элемента в конец списка

sp.insert(0, "first") # добавление элемента в список, с указанием места 
print(sp)
sp.remove(True)

del sp[0]

print(sp)

sp = list()
sp = [-1, True, "hello", 5.77, 8.999, "world"]

# print(sp)
# print(sp[2:5])

# for i in range(len(sp)):
# print(f"{i} - {sp[i]}")

# for el in sp:
# print(el, end = ' ')

# print(end = '\n')

sp.append('last')
sp.insert(0,'first')
# print(sp)

sp.remove(True)
del sp[0]
# print(sp)
a = sp.pop()
# print(a)
# print(sp)

t = tuple(sp)
# print(t)
# print('hi' in t)
# print('hello' in t)

d = {}
d['дядя ваня'] = 8645464
d['дядя вася'] = 21313231321
# print(d)
# print(d.keys())
# print(d.values())
# for i in d:
# print(i)
# for key,value in d.items():
# print(f"{key} - {value}")

s = {1,1,5,1,1,5,5,8,8,8,1,1,1,8,8}

s.add(7)
print(s)
s.discard(1)
s.discard(2)

print(s)