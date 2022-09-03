elements = [9, 6, 5, 0, 8, 2, 7, 1, 3, 4]

for index in range(len(elements)):
    if (index != 0) and (elements[index] < elements[index-1]):
        for i in range(len(elements[:index])):
            if elements[index] < elements[i]:
                elements.insert(i, elements.pop(index))
            else:
                continue
    elif index != 0:
        pass
    else:
        continue
print(elements)