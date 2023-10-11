def every_third_element(input_list):
    new_list = input_list[2::3]
    return new_list

def print_list(my_list):
    for item in my_list:
        print(item)

user_list = input("Введіть список елементів: ").split()
result_list = every_third_element(user_list)
print("Початковий список:")
print_list(user_list)

print("Кожен третій елемент:")
print_list(result_list)