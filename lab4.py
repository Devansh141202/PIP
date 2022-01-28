dictionary1 = {
    'fname': 'Devansh',
    'lname': 'Nirmal',
    'address': {'District': 'Jamnagar', 'pincode': 361001},
    'skill': ['JavaScript', 'React', 'Node', 'MongoDB','Python']
}

for key in dictionary1:


    # -------------------------( Task 1 )-----------------------------#
    '''
    we will first check that dictionary contain skill or not if yes
    then we will check if there is only one element then it will be middle 
    element it self other-wise we will divide total length by 2.
    '''
    
    if key == 'skill':
        list = dictionary1['skill']
        if int(len(list)) < 2:
            mid = 0 #because in that case first element become mid elementt
        elif len(list)%2==0:
            mid = int((len(list) / 2)-1)
        else:
            mid = int((len(list) / 2))
        print(list[mid])

#-------------------------( Task 2 )-----------------------------#      
        if 'Python' in list:
            print("The person have python as skill")


#-------------------------( Task 3 )-----------------------------#
        if "Javascript" and "React" in list:
            print("He is a Frontend Developer ")
        elif 'Python' and "MongoDB" and 'Node' in list:
            print('He is a Backend Developer')
        elif 'Node' and "React" and 'MongoDB' in list:
            print('He is a full stack Developer')
        else:
            print("Not known")
       
#-------------------------( Task 4 )-----------------------------#
even = 0
odd = 0

for i in range(101):
    if i%2==0:
        even += i
    else:
        odd += i
print("Sum of even in 0 to 100 is = ",even)
print("Sum of Odd in 0 to 100 is = ",odd)


#-------------------------( Task 5 )-----------------------------#
def checking_list(lists):
    if len(set(lists)) == len(lists):
        print("In ",lists," All elements are unique.")
    else:
        print("In ",lists," All elements are not unique.")

list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 3, 4, 5]
checking_list(list1)
checking_list(list2)


#-------------------------[ Task 6 ]-----------------------------#
def check_datatype(checking_list):
    datatype_Of_first = type(checking_list[0])
    for x in checking_list:
        if type(x) == datatype_Of_first:
            continue
        else:
            return print("Datatype of all elments is not same")
    return print("Datatype of all elments is same")  


list01 = ['D', 'e', 'v', 'a', 'n', 's', 'h']
list02 = [1,[1.1,'Devansh'],'w']

check_datatype(list01)
check_datatype(list02)



#-------------------------[ Task 7 ]-----------------------------#
from keyword import iskeyword
def check_variable(variable):
    if variable.isidentifier() and not iskeyword(variable):
        print("Variable name is valid")
    else:
        print("Varible name is invalid")


check_variable('%Devansh')
check_variable('_Devansh')
check_variable('12Devansh')
check_variable('Devansh')
