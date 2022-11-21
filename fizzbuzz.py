for n in range(1,106):
    if n%3==0:
        print('Fizz')
    if n%5==0:
        print('Buzz')
    elif n%3==0 and n%5==0:
        print('FizzBuzz')
        
    else:
        print(n)