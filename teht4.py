with open ("t4.txt") as file:

    list = [line.rstrip() for line in file]

list.sort()
list.sort(key=len)

print(list)



with open(r"t4uusi2.txt", "w") as tiedosto:
    tiedosto.write('\n'.join(list))
