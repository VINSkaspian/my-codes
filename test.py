# ЗАГОЛОВОК
print("FREE WHISKEY FOR YO DEAR FRIEND!))))")
answer = input("Do you want some whiskey?") #
# answer умова = присвоєння input (вивід питання в консоль)
if answer == 'yes':
# метод if-якщо answer умова == порівняння 'yes':
    name = input("what is yor name? ")
# name ім'я = присвоєння input ("вивід питання в консоль ")
    age = int(input("how old are you?"))
# age вік = присвоєння int функція що приймає значення або
# рядок з комою і повертає ціле число(input("вивід питання в консоль "))
    if age >=18 :
# метод if-якщо age вік >= більше ніж 18 змінна:
        print("Super! get yor whiskey !)))", name)
# print('Вивід повідомлення', name змінна ім'я)
    else:
# else: якщо
        print('GO TO SCHOOL KID!!!!!')
# print('Вивід повідомлення')
else:
# else: якщо
   print("Bye!))))")
# print('Вивід повідомлення')