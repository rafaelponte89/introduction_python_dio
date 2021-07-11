a = {10,2,3,4,5}
b = {5, 6, 7, 8}

uni = a.union(b)
int = a.intersection(b)
dif = a.difference(b)
dif2 = b.difference(a)
sd = a.symmetric_difference(b)
print('Union : {}'.format(uni))
print('Intersection : {}'.format(int))
print('Difference A - B : {}'.format(dif))
print('Difference B - A : {}'.format(dif2))
print('Dif Simetric: {}'.format(sd))
c = {1,2,3}
d = {1,2,3,4,5}
subcd = c.issubset(d)
print('C is subset of D: {}'.format(subcd))
spset = d.issuperset(c)
print('D is superset of C: {}'.format(spset))
lista = ['rato','boi','tigre']
lista = lista *3

print(lista)
set_animal = set(lista)
print(set_animal)
# conjunto = {1,2,3,4}

# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)
