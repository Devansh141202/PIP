def most_common(List):
    count = 0
    element = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> count):
            count = curr_frequency
            element = i
 
    print(element)
List = ['dog', 'cat', 'dog']
most_common(List)