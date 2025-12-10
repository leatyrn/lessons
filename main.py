import time
start = time.time()
right = 0
answer1 = input("Яке середнє значення цих чисел?(5,6,4): ")
if answer1 == "5":
    print("Вірно")
    right +=1
else:
    print(f"Невірно, правильна відповідь: 5")
    right +=0
answer2 = input("Сількки буде 0/16?: ")
if answer2 == "0":
    print("Вірно")
    right +=1
else:
    n = 0/16
    print(f"Невірно, правильна відповідь, {n} ")
    right +=0
answer3 = input("Розв'яжи р-ня x-25=0 ")
if answer3 == "25":
    print("Вірно")
    right +=1
else:
    print("Невірно, x = 25")
    right +=0
end = time.time()
actual = end - start
print(f"Час витрачено на тест: {actual/60:.2f} секунд")
if right == 0:
    print(f"На другий раз пощастить, правильних: {right}")
elif right == 1:
    print(f"Ну це хоч щось, правильних: {right}")
elif right == 2:
    print(f"Клас, правильних: {right}")
else:
    print(f"Та ти відмінник! Правильні усі!")

