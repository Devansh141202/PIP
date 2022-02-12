a = ("Str",)
print(type(a))
b = list(a);
print(type(b))
b.append('Devansh')
b.remove('Str')
print(b)
c = tuple(b)
print(type(c))