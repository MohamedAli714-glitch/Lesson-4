Squareroot=int(input("Enter a number to find its square root: "))
if Squareroot < 0:
    print("Sorry, square root of negative numbers is not defined in real numbers.") 
else:
    result = Squareroot ** 0.5
    print("The square root of", Squareroot, "is", result)

print("Check it on your calculator to verify the result.")