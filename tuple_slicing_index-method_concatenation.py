#                 Tuple 
tup=(1, 2, 76, 342, 32, "Green", True)
# tup[0]=90         # TypeError: 'tuple' object does not support item assignment(We cannot change the value of tuple))
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[1:])
# print(tup[34])           # It through error because index is out of range

if 342 in tup:
    print("Yes it's in tuple")

if "Green" in tup:
    print("Yes Green is present")


#                 Tuple Slicing (skip index)
animals=("cat","dog","bat","mouse","pig","horse","donkey","goat","cow")
print(animals[1:8:3])



#                 Tuple Methods( change content of tuple))
countries=("spain","italy","india","england","germany")
temp=list(countries)
temp.append("Pakistan")
temp.pop(2)
temp[3]="Finland"
countries=tuple(temp)
print(countries)



#                 Tuple Concatenation
tup1=(0,1,2,3,4,5)
tup2=("python","java","c++")
tup3=tup1+tup2
print(tup3)



#                 Index Method in Tuple
#                 Syntax: tuple.index(element, start, end)
tup=(1,2,3,5,5,6,7,5,9,10)
res=tup.index(5, 2,9)
print("Count of 5 : ",res)