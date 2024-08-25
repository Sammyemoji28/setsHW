
aSet = {14,6,4,27,86,4,7,6,4}

print(aSet)

if 6 in aSet:
    print("That number is in the set!")
else:
    print("That number isn't in the set!")

if 16 in aSet:
    print("That number is in the set!")
else:
    print("That number isn't in the set!")

print(aSet)

aSet.discard(4)
print(aSet)

aSet.discard(7)
print(aSet)

set1 = {4,6,2,4,53,3,46,48,9}
set2 = {4,7,64,46,7,1,47,9,5}

print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set1.difference(set2))
print(set2 - set1)

print(set1.symmetric_difference(set2))
print(set2 ^ set1)