tested_number = int(input())
tested_number_is_prime = True
for i in range(2, tested_number):
    if tested_number % i == 0:
        tested_number_is_prime = False
        break
print(tested_number_is_prime)
