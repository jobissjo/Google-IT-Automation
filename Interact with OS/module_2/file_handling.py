
with open('myfile.txt', 'r') as file:
    print(file.readlines())


with open('myfile.txt', 'r') as file:
    for line in file:
        print(line.strip().upper())

with open('novel.txt', 'w') as file:
    file.write('It was a dark and stromy night')