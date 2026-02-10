numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Sort ascending
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Ascending order:", numbers)

# Sort descending
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Descending order:", numbers)
