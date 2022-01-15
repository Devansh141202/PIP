dic = {
    'name': 'Devansh',
    'id':'61',
    'name':'Devansh'   
}
fin_max = max(dic, key = dic.get)
print(fin_max)
# List = list(dic.items())
# print(List)
# def most_common(List):
#     count = 0
#     element = List[0]
     
#     for i in List:
#         curr_frequency = List.count(i)
#         if(curr_frequency> count):
#             count = curr_frequency
#             element = i

#     print(element)
#     most_common(List)