list_loc = []
name_list = [1.2, 2, 'Cheburek']
for name in name_list:
    loc = f'My name is {name}'
    a = list_loc.append(loc)
    print(loc)

biblioteka = {"factor": list_loc, "risk": name_list, "example": 123}

abiblio = biblioteka.get("factor")

print(abiblio)

*names, = 'Test', 'No test', 'Data'

# прочитай про * как создавать списки

print(names)

*caramba, = 'Boroda', 'Dead man', 'Holy land'
print(caramba)
