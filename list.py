numbers = [1,2,4,6,11,22,23]

print("hello")

large = numbers[0]

for number in numbers:
    check = number
    if check>large:
        large = check

print(large)
