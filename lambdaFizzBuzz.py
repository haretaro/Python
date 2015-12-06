import functools
fizzbuzz = lambda n : 'Fizz' * (n%3==0) + 'Buzz' * (n%5==0) + (n%3!=0)*(n%5!=0) * str(n)
for x in range(30):
    print(fizzbuzz(x))

