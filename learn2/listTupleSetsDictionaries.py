"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)

#akses member of list
print(thislist[1])

#change value member
thislist[1] = "mango"
print(thislist[1])
print(thislist)

#akses member of list with range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1:5])

#add list
thislist.append("orange")

#add item the second position
thislist.insert(1, "grape")
print(thislist)


#---------Tuple
print("------")
print("TUPLE")
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#akses value member
print(thistuple[1])

#change value and add member will error
#thistuple[1] = "kiwi" <-- ERROR

#----------SETS
print("------")
print("SETS")

thisset = {"apple", "banana", "cherry"}
print(thisset)

#akses member
for x in thisset:
  print(x)

#check value exist
print("banana" in thisset)  
print("orange" in thisset)  

#add items 
thisset.add("orange")
print(thisset)

#add multiple items
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

model = thisdict.get("model")
print(model)

#change data
thisdict["model"] = "BARU DAH"
model = thisdict.get("model")
print(model)

