elements = [9, 6, 5, 0, 8, 2, 7, 1, 3, 4]
sorted_array = []
for index in range(len(elements)):
    if (index != 0) and (elements[index] < elements[index-1]):
        for i in range(len(elements[:index])):
            if elements[index] < elements[i]:
                tmp = elements[index]
                del(elements[index])
                elements.insert(i, tmp)
            else:
                continue
    elif index != 0:
        pass
    else:
        continue
print(elements)