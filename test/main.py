# hello

# a = 5

# if a > 2:
#     print("Число більше 2")



# print("Число більше 2") if a > 2 else print("Число менше 2")


# my_string = "Hello world!!!"
# for char in my_string:
#     # print(f"Літера '{char}'")
#     print(char, end="|")

# my_string = "Який чудовий сьогодні день!"
# count = 0

# for char in my_string:
#     if char == "о":
#         count += 1 # count = count + 1

# print(f"Нарахували таку кількість літер 'о': {count}")


# my_string = "Який чудовий сьогодні день!"
# count = 0

# for char in my_string:
#     count += 1


# print(f"Кількість символів: {count}")

# my_string = "Який чудовий сьогодні день!"
# for i, char in enumerate(my_string, start=1):
    # print(f"Індекс символу '{char}' - {i}")
#     pass

# print(f"Індекс символів: {i} - {char}")


# for i in range(5):
#     print(i)

# for i in range(20):
#     if i % 3 == 0
#     print("Це чимло ділиться на 3 без залишку")
#     continue

#     print(f"Поточне число - {i}")
# else:
#     print(Чи надрукує щось після continue)

# my_string = "Привіт"
# for _ in range(15):
#     print(my_string)

# Роздрокувати числі від до які ввів користувач
# a = input("Введіть поачток проміжу: ")
# b = input("Введи кінець проміжку: ")

# if a.isdigit() and b.isdigit():
#     a = int(a)
#     b = int(b)

#    for i in range(a, b+1):
#         print(i)
# else:
#     print("Ви ввели не число")

a = int(input())
b = int(input())
c = int(input())
d = int(input())

#print header
print(end = '\t')
for i in range(c, d + 1) :
    print(i, end = '\t')
print("")

#print table
for i in range(a, b + 1) :
    print(i, end = '\t')
    for j in range(c, d + 1) :
        print(i * j, end = '\t')
    print("")