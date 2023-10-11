def operation(list, value):

    for i in range(len(list)):
        if list[i][1] == value:
            list.remove(list[i])
            break
    return list

list = []

print("Введіть список:")
for item in input().split():
    list.append([int(item.split(":")[0]), int(item.split(":")[1])])

print("Список:")
for item in list:
    print(item)
print("Введіть значення, за яким виконується операція:")
value = int(input())

new_list = operation(list, value)

print("Новий список:")
for item in new_list:
    print(item)

