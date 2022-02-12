personalDetails = {
    'name' : 'Devansh', 
    'add' : 'Jamnagar'
}
Clg = {
    'name' : 'Charusat',
    'id' : '061'
}

# personalDetails.update(Clg)
# print(personalDetails)
# personalDetails.pop('name')
# personalDetails.popitem
# print(personalDetails)
# print(personalDetails.keys())
# print(personalDetails.fromkeys(personalDetails, Clg))
# print(personalDetails)
print(Clg.setdefault('AB', 'Devansh'))
print(Clg)