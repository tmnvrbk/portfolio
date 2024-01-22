def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


iteration = 1

while True: 
    if is_prime(iteration): 
        print (f"{iteration} is Fizzbuzz")
    elif iteration % 2 == 0: 
        print (f"{iteration} is Fizz")
    else: 
        print (f"{iteration} is Buzz")



    iteration += 1
    if iteration == 50: 
        break