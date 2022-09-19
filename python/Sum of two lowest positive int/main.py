def sum_two_smallest_numbers(numbers):
    #your code here

    numbers.sort()

    return numbers[0] + numbers[1]



num1 = [5, 8, 12, 18, 22]
num2 = [7, 15, 12, 18, 22]
num3 = [25, 42, 12, 18, 22]

print(sum_two_smallest_numbers(num1))
print(sum_two_smallest_numbers(num2))
print(sum_two_smallest_numbers(num3))