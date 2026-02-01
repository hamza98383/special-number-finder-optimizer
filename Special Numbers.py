import time
import math

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_palindromes(m, n):
    palindromes = []

    # Generating palindromic numbers with odd length
    for i in range(1, 10**(len(str(n)) // 2)):
        palindrome_str = str(i) + str(i)[-2::-1]  # Generate palindrome with odd length
        palindrome = int(palindrome_str)
        if m <= palindrome <= n:
            palindromes.append(palindrome)

    # Generating palindromic numbers with even length
    for i in range(1, 10**(len(str(n)) // 2)):
        palindrome_str = str(i) + str(i)[::-1]  # Generate palindrome with even length
        palindrome = int(palindrome_str)
        if m <= palindrome <= n:
            palindromes.append(palindrome)

    return palindromes

def find_special_numbers(m, n):
    special_numbers = []

    # Generate palindromic numbers within the range [m, n]
    palindromes = generate_palindromes(m, n)

    # Filter palindromes to find special numbers (palindrome and prime)
    for palindrome in palindromes:
        if is_prime(palindrome):
            special_numbers.append(palindrome)

    return special_numbers

# Input two positive numbers m and n (where m is smaller than n)
m = int(input("Enter the smaller number (m): "))
n = int(input("Enter the larger number (n): "))

start_time = time.time()

special_numbers = find_special_numbers(m, n)

end_time = time.time()

print(f"Total number of special numbers lying between {m} and {n} is: {len(special_numbers)}")

if len(special_numbers) > 6:
    print(f"First three and last three special numbers: {special_numbers[:3] + special_numbers[-3:]}")
else:
    print(f"Special numbers: {special_numbers}")

print(f"Time taken to produce the result: {end_time - start_time:.4f} seconds")
