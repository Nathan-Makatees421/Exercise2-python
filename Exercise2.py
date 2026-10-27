x= 5
y= 4

x = x + 3
y = y * 2
result = x / y

print(result)

a = 10
b = 8
c = 4
condition1 = a > b
condition2 = b == 0
condition3 = c <= a
final_condition = condition1 or (condition2 and condition3)

print(final_condition)
  
score = int(input("test score:"))

if score >= 90-100:
  print('A')
elif score >= 80-89:
  print('B')
elif score >=70-79:
  print ('C')
elif score >=60-69:
  print('D')
else: 
  print('F')

num1 = float(input("enter a first number:"))
num2 = float(input("enter a second number:"))
operation = input("enter an operation(+, -, *, /):")

if operation == "+":
  result = num1 + num2
  print("result" , result)
elif operation =="-":
  result = num1 - num2
  print("result" , result)
elif operation == "*":
  result = num1 * num2
  print("result" , result)
elif operation == "/":
  if num2 == 0:
    print("error: divsion by zero not allowed.")
  else:
    result = num1 / num2
    print("result" , result)
else:
  print("invalid operation.")