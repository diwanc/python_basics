list1 = [3,'rer',9.67]

print(list1)

print(type(list1))

#nested lists

list2 = [1, 4, 6, list1]
print(list2)

tup1 = (1,3,'ty')

list3 = [list2, tup1]
print(list3)

tup2 = (tup1,list1)

print(tup2)

list1[0] = 'chnaged list element'

print(list1)

print(tup2)

print(list3[1][2]) #access nested list elements

#list concat
list4 = list1 + list(tup1)
print(list4)

# multuply list
tup3 = tup2 * 2
print(tup3)

# multuply list
tup3 = tup2 * 0
print(tup3)

list3.append('object')
print(list3)

print(list3.pop(1))
print(list3.remove('object'))
print(list3)