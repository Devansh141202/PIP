# Set

# a. Write a Python program to add member(s) in a set and clear a set

# S=set()
# S.add(1)
# S.update([2,3,4,5])
# print(S)

# L={1,2,3,4}
# L.add(5)
# print(L)



# b. Write a Python program to remove an item
#  from a set if it is present in the set.

# S=set()
# S.add(1)
# S.update([2,3,4,5])
# print(S)

# S.remove(2)
# print(S)

# S.remove(6)
# print(S)



#c. Write a Python program to create an intersection, 
# Union, difference of sets.

# L={1,2,3,4}
# P={4,5,6,7,8}

# print(P.union(L))
# print(P.intersection(L))
# print(L.difference(P))



# d. Write a Python program to find maximum and the 
# minimum value in a set.

# Set = {4,44,60,8,0,100}
# print(Set)
# print(max(Set))
# print(min(Set))



# e. Write a Python program to find the most common
#  elements and their counts from list, tuple, dictionary.


# list
# def most_common(List):
#     count = 0
#     ele = List[0]
     
#     for i in List:
#         curr_frequency = List.count(i)
#         if(curr_frequency> count):
#             count = curr_frequency
#             ele = i
 
#     print("Common element is :", ele,"(",count,")")

# List = ['red','green','blue','red','red']
# most_common(List)



# Tuple
# tuple = ("red", "green", "blue","green")

# def most_common(List):
#     count = 0
#     ele = List[0]
     
#     for i in List:
#         curr_frequency = List.count(i)
#         if(curr_frequency> count):
#             count = curr_frequency
#             ele = i
 
#     print("Common element is :" ,ele,"(",count,")")
    
# most_common(tuple)



#Dictionary
# dic = {
#     'name1':'Devansh',
#     'name2':'riya',
#     'name3':'Devansh',
#     'name4':'sia',
#     'name5':'Devansh'}

# def frequncyDict(dic):
#     count = 0
#     values = list(dic.values())
#     print(dic)
#     value  = values[0]  
#     for i in values:
#         cur_freq = values.count(i)
#         if (cur_freq>count):
#             count = cur_freq
#             v = i

#     print(" Common element is :" ,v ,"(",count,")")
    
# frequncyDict(dic)



# Devansh Nirmal
# 20CE061
# Github Link = https://github.com/Devansh141202/PIP_Assignment


