def find_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
even = find_even_numbers(n)
print(even)

