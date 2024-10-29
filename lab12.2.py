import random
import string

def generate_car_number():
    number_part = str(random.randint(1000, 9999))
    letter_part = ''.join(random.choices(string.ascii_uppercase, k=3))
    return f"{number_part} {letter_part}"

def generate_n_numbers(n):
    return [generate_car_number() for _ in range(n)]

N = 5
car_numbers = generate_n_numbers(N)
print(car_numbers)
