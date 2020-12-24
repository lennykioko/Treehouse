with open('comp1.txt') as file1:
    comp1 = [line.rstrip('\n') for line in file1]

with open('comp2.txt') as file2:
    comp2 = [line.rstrip('\n') for line in file2]

uniques = []
for item in comp2:
    if item not in comp1:
        uniques.append(item)
        with open("unique.txt", "a+") as file:
            file.write(f"{item}\n")
