file_path = 'data.txt'
animals = {}
sol = ""

with open(file_path, 'r') as file:
    content = file.read().split(" ")

for i in content:
    if not animals.get(i):
        animals[i] = 1
    
    elif animals.get(i):
        count = animals.get(i)+1
        animals[i] = count

for i in animals:
    sol+=i + str(animals.get(i))
print(sol)