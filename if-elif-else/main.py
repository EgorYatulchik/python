
# if number == 5:
#     print("Це число 5")
# elif number > 0:
#     print("Дане число більше нуля")
# elif number < 0:
#     print("Дане число мешне нуля")
# else:
#     print("Це нуль")
# number = 5

# if number == 5:
#     print("Це блок == 5")
#     print("Це число 5")
#     print("1")
#     print("2")
#     print("3")

# if number > 0:
#    print("Це блок > 0")
#     print("Дане число більше нуля")

# if number < 0:
#     print("Це блок < 0")
#     print("Дане число мешне нуля")

# print("Це нуль")


# my_string = " "

# if my_string :
#    print("Рядок не пустий")
# else :
#    print("Рядок пустий")

# print(bool("")) # False
# print(bool(None)) # False
# print(bool(0)) # False
# print(bool(False)) # False
# print(bool(0.0)) # False

# my_string = ""
# if my_string:
#     print("Рядок не пустий")
# else :
#     print("Рядок пустий")

# if not my_string:
#     print("Рядок пустий")

# age = int(input("Введіть свій вік: "))
# print("Повнолітній") if age > 18 else print("Не повнолітній")

# name = "Тарас"
# age = None
# has_driver_licence = True

# if age > 18 and has_driver_licence:
# if age > 18 and has_driver_licence == True:
# if age > 18 and has_driver_licence is True:

# if age and age > 18 or has_driver_licence:
#     print(f"{name}, Вітаю, ти можеш їхати")

x = int(input("Найбільше число"))
y = int(input("Середне число"))
z = int(input("Найменше число"))

if x > y and x > z :
   print("Число більше", 3)
elif y > x and y > z:
   print("Число більше", 2)
elif z > x and z > y:
   print("Найменше число", 1)
else :
   print("Є одинакові числа")