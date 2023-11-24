file_path = 'data.txt'
with open(file_path, 'r') as file:
    content = file.read().split("\n")

valid = []
invalid = []
def is_valid(password, min, max, letter):
    if password.count(letter) >= min and password.count(letter) <= max :
        return True
    return False

for i in content:
    i = i.split(" ")

    min = int( i[0].split("-")[0])
    max = int( i[0].split("-")[-1])

    letter = i[1][0]

    password = i[2]
    if is_valid(password, min, max, letter):
        valid.append(password)
    else:
        invalid.append(password)
        
print(invalid[12])