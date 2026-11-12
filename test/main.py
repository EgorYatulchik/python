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
#     # print(f"Індекс символу '{char}' - {i}")
#     pass

# print(f"Кількість символів: {i} - {char}")


# for i in range(1, 10, 2):
#     print(i)


# for i in range(1, 10):
#     if i == 50:
#         print("Цикл не завершено")
#         break
# else:
#     print("Цикл завершено!")

# print(f"{i = }")

# for i in range(20):
#     if i % 3 == 0:
#         print("Це число ділиться на 3 без залишку")
#         continue

#     print(f"Поточне число - {i}")
# else:
#     print("Чи надрукує щось після continue?")

# my_string = "Привіт"
# for _ in range(15):
#     print(my_string)


# Роздрукувати числа від до які ввів користувач
# a = input("Введи початок проміжку: ")
# b = input("Введи кінець проміжку: ")

# if a.isdigit() and b.isdigit():
#     a = int(a)
#     b = int(b)

#     for i in range(a, b+1):
        # if i % 2 == 1:
#             print(i)
# else:
#     print("Ви ввели не число")

# for i in range(1, 101, 2):

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# #print header
# print(end = '\t')
# for i in range(c, d + 1) :
#     print(i, end = '\t')
# print("")

# #print table
# for i in range(a, b + 1) :
#     print(i, end = '\t')
#     for j in range(c, d + 1) :
#         print(i * j, end = '\t')
#     print("")

# my_string = "привіт світ"
# my_string[0]

# a = 2
# while a < 6:
#     a += 1 
#     print(f"{a = }")

# my_string_1 = "Привіт мій чудовий світ!"
# my_string_2 = "А це інший допомідний рядок."
# print(len(my_string_1))
# i = 1
# while len(my_string_1) < 40:
#     my_string_1 += my_string_2[i]
#     i += 1

# print(f"{my_string_1 = }")
# print(f"{len(my_string_1)}")

# while True:
#     my_string = input("Введи своє запитання або введи exit для виходу: ")
#     if my_string.lower() == "exit":
#         print("Дякую що скористались нашими послугами")
#         break
#     print(f"Ваше запитання -> {my_string}")

# print("Програма завершилась")

# numbers = [i for i in range(20)]
# print(numbers)

# Порахувати середнє арифметичне всіх чисел кратних 3 з певного інтервалу
# sum = 0
# count = 0
# for i in range(100):
#     if i % 3 == 0:
#         count += 1
#         sum += i

# avg = sum / count
# print(f"Середнє арифметичне дорівнює {avg}")

# while True:
#     number = int(input("Введи число: "))

#     if number > 100:
#         break

#     if number > 20:
#         print(number)

# for i in range(20):
#     print(f"{i = }")
#     for j in range(2):
#         print(f"{j = }")
#         if j > 3:
#             break
#         break

while True:
    number = input("Введи число в діапазоні 1-999: ")
    if not number.isdigit() or int(number) < 1 or int(number) > 1000:
        print("Ввели не число або число поза межами діапазону. Спробуйте ще раз")
        continue

    number = int(number)
    if number < 10:
        name = "Одноцифрове"
    elif number < 100:
        name = "Двоцифрове"
    else:
        name = "Трицифрове"

    is_odd = True if number % 2 == 0 else False
    print(f"Число {"парне" if is_odd else "непарне"} {name.lower()}")
    # print(f"Число {"парне" if number % 2 == 0 else "непарне"} {name.lower()}")
