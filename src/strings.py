str1 = "Test"
str2 = "Tes't2"
int1=143

print(str(int1)+str1+str2)
print(list(str1))

print(str1[0])

print(str1[0-len(str1)]) #reverse index

#str1[0]='r' #error. str is immutable


#string slicing
str3 = "Hello World"
print(str3[0:5])
print(str3[-11:5]) #same result
print(str3[-11:-5])

#print(str3[22]) # out of range error
#print(str3[-12]) # out of range error

print(str3[7:]) # 7 till last
print(str3[:3]) # first to 3-1

print(str3[0:5:2]) #step 2

print(str3.upper())

print(type(print))
print(type(str.upper))

splitstr = str3.split()
print(type(splitstr))
print(splitstr)

splitstr = str3.split(None,0)
print(splitstr)

splitstr = str3.split('o',2)
print(splitstr)

print(str3.count('o', 0, 6))
print(str3.count('l')) #count of l
print(str3.count('l', 0, 3)) # count of l in the first 3 positions
print(str3.count('l', 0, 4))