number=int(input("Enter a number"))

for i in range(1,number):
    if i% 3 == 0:
        print(str(i) + "- Fizz")
    if i% 5 == 0:
        print(str(i) + "- Buzz")
    if i% 3 == 0 and i% 5 == 0:
        print(str(i) + "- FizzBuzz")
    else:
        print(str(i))
    