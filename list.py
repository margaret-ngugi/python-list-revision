# append()
#It is used to add elements in a list
list=["python",3.14,2022,"hello","Faith"]
list.append("Maggie")
print(list)

#len()
#It is used to determine how many items a list has
list=["mango","apple","banana","orange"]
print(len(list))

#count()
#Returns count of how many times item occurs in list
list = ["mango","apple","banana","orange","banana"]
list.count("banana")
print(list)

#insert()
#Inserts an item to index position in a list
list = ["mango","apple","banana","orange","banana"]
list.insert(0,"ovacado")
print(list)

#sort()
#sorts the value in a list in an ascendng manner
list = ["mango","apple","banana","orange","banana"]
list.sort()
print(list)

#extend()
#adds a new list to the current list
list = ["mango","apple","banana","orange","banana"]
list.extend(["passion","lemon"])
print(list)

#reverse()
#It reverses the order of items in a list
list = ["mango","apple","banana","orange","banana"]
list.reverse()
print(list)

#remove()
#revoves the first occurence of a given item from the list
list = ["mango","apple","banana","orange","banana"]
list.remove("banana")
print(list)

#pop()
#removes and returns the last element in a list
list = ["mango","apple","banana","orange","banana"]
list.pop()
print(list)

#del()
#It is used to delete items from a list

sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)

#To change the value of a specific item, refer to the index number:
list = ["mango","apple","banana","orange","banana"]
list[1] = "berry"
print(list)
#It has changed  the item in index 1  with berry

#another example 
list = ["mango","apple","banana","orange","banana"]
list[1:3] = ["blackcurrant", "watermelon"]
print(list)

#type()
#It is used to get the type of the object
list = ["mango","apple","banana","orange","banana"]
print(type(list))

#Accessing items from a list using indexing
list = ["mango","apple","banana","orange","banana"]
print(list[3])

#Another example
list = ["mango","apple","banana","orange","banana"]
print(list[1:4])


#Joinig list
#using + operator
list1 = ["Maggie", "Faith", "Sharon"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Another way to join two lists is by appending 
list1 = ["Maggie", "Faith" , "Sharon"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# you can use the extend() method,
list1 = ["Maggie", "Faith" , "Sharon"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


#list comprehension - is a concise way of creating lists from the ones that already exist.

list = ["mango","apple","banana","orange","banana","onion"]
newlist = []

for x in list:
  if "e" in x:
    newlist.append(x)

print(newlist)

#We can also make copies from a list using copy()method


#copy()
fruits = ["mango","apple","banana","orange","banana"]
newfruits= fruits.copy()
print(newfruits)


#what I have learned from list:
#Lists are used to store multiple items in a single variable.
#list are changeable-we can be able to add,remove or change items from the list.
#list are ordered-if you add items to a list,they will be added at the end of the list.
#list allow duplicates
#we can be able to access items from a list by refering to the index number
#we can be able to change items from a list by refering to the index number and also using the insert()method
#we add items to the list using the append(),extend(),insert() method
#we remove list items by using the pop(),del(),clear(),remove() method
#we can also loop through a list by using a for loop
#we can also sorts ,join, reverse a list.






