def sum_of_prime_factors(n):
  x = 0
  for i in range(2, n):
    if n % i == 0:
      x += i
  return x

#Test Cases:

print(sum_of_prime_factors(91))

print(sum_of_prime_factors(33))

print(sum_of_prime_factors(100))
