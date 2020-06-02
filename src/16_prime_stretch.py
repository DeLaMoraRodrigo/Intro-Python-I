def is_prime():
    num = input("Enter a number: ")
    num = int(num)

    if (num > 1):
        for i in range(2, (num + 1)): 
            if (num % i) == 0 and i < num:
                print(f"{num} is not a prime number")
                break
            elif i == num:
                print(f"{num} is a prime number")
                break                
    else:
        print(f"{num} is not a prime number")

is_prime()