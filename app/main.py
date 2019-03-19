
numbers = []

while(True):
    number = int(input("Введите число: "))
    if number == 0:
        break

    numbers.append(number)

numbers.sort()

for i, number in enumerate(numbers):
    print(f"{i+1}.{number}")

print("----------------")
print(f"Сумма: {sum(numbers)}")
