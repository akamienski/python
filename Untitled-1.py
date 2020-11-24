num1 = 1.5
num2 = -6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The {3} of {0} and {1} is {2}'.format(num1, num2, sum, sum))

#num = float(input("Enter a number: "))
if sum > 0:
   print("Positive number")
elif sum == 0:
   print("Zero")
else:
   print("Negative number")

num=12

for i in range(1, 11):
    print(num, 'x', i, '=', num*i)