
#converting a list to a set :0

list = [14,5,35,79,4,9,23]

#method1

sampleSet = set(list)

print(sampleSet)
print(type(sampleSet))

#method2

myset = {12,3,2,4,63,42,34,5,5,4,6,44,7,3,4,45}

print(myset)
#print(myset[6]) : no index numbers for sets, error

#checking for an item in sets

if 34 in myset:
    print("Number exists!")
else:
    print("Number doesn't exist!")

if 46 in myset:
    print("Number exists!")
else:
    print("Number doesn't exist!")

#adding items to set

myset.add(11)
print(myset)

#removing items from set
#method1

myset.remove(45)
print(myset)

#myset.remove(1) cant remove stuff that doesnt exist if you need to check
#method2

myset.discard(2)
print(myset)

myset.discard(1) #doesnt give an error even if number isnt there
print(myset)

#set operations

setA = {1,45,3,5,64,5,1,2,90}
setB = {1,3,40,3,53,6,34,9,6}

#1 - union

print(setA.union(setB))
print(setA | setB)

#2 - intersection

print(setA.intersection(setB))
print(setA & setB)

#3 - difference

print(setA.difference(setB))
print(setB - setA)

#4 - symmetric difference

print(setA.symmetric_difference(setB))
print(setB ^ setA)