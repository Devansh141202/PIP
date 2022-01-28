from keyword import iskeyword

dict  ={
    'fname':'Yash',
    'lname':'Narodia',
    'address':{
    'Street Name':'royal mint',
    'Street No':'21st',
    'pincode':361142
    },
    'skill':['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    }

for key in dict:
#-----------------------Skills present in person-------------------
    #-------------------(1)printing middle skill----------------------
    if (key=='skill'):
        list = dict['skill']
        if int(len(list))<2:
            middle = 1
        else: 
            middle = int((len(list)/2))
        print(list[middle])
    #-------------------(2)checking if skill contain python------------
        for item in list:
            if(item =='Python'):
                print('Python Present')
            else:
                continue
    #-------------------(3)What kind of developer----------------------
        if("Javascript" and "React"  in list):
            print("He is a Frontend Developer ")
        elif('Python' and "MongoDB" and 'Node' in list):
            print('He is a Backend Developer')
        elif('Node' and "React" and 'MongoDB' in list):
            print('He is a full stack Developer')
        else:
            print("Unknown title")
    else:
        continue
#-----------(4) Sum of odd and even numbere from 0 to 100---------------
odd,even = 0,0
for i in range(101):
    if (i%2==0):
        even+=i
    else:
        odd+=i
print('Even sum = ',even)
print('Odd sum = ',odd)
#---------------(5) All items are unique in the list-----------------------
def Unique_list(list):
    if(len(set(list)) == len(list)):
        print("All elements are unique.")
    else:
        print("All elements are not unique.")

list1 = [1,2,3,4,5,6]
list2 = [1,2,3,3,4,5]
Unique_list(list1)
Unique_list(list2)
#-------------(6) All item of the list have same data type-----------------
def same_DataType(list):
    res = True
    for element in list:
        if not isinstance(element, type(list[0])):
            res = False 
            break
    print("all element have same data type" if res==True else "all element have different data type")

list3 = [1,'w',[1,2,'asdad'],1.4]
list4 = ['w','q','w','a']
same_DataType(list3)
same_DataType(list4)
#------------(7) if provided variable is a valid python variable-----------
def valid_Variable(variable):
    if(variable.isidentifier() and not iskeyword(variable)):
        print("Name is valid variable name")
    else:
        print("Name is invalid varible name")
valid_Variable('yxz')
valid_Variable('_axc')
valid_Variable('12msa')
valid_Variable('%was')