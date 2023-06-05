def is_perfect_number(number):
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    if divisor_sum == number:
        return True
    else:
        return False

#number = 28  # Example number
number1 = int(input())
if is_perfect_number(number1):
    print(f"{number1} is a perfect number.")
else:
    print(f"{number1} is not a perfect number.")

    
