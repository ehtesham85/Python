l=[11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.append(7)                # add 7 to the end of the list
print(l)
l.sort()                   # sort the list Accending Order wise
print(l)
l.sort(reverse=True)       # sort the list Decending Order wise
print(l)
print(l.index(1))
print(l.count(1))
m=l.copy()
m[0]=0
l.insert(5,99)



#            Concatenating two list
m=[900,100,1100]
k=l+m
print(k)

colors=["voilet","indigo","blue","green"]
colors2=["yellow","orange","red"]
print(colors+colors2)
