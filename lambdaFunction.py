# lambda functions are used to create small anonymous functions in Python. They can take any number of arguments but can only have one expression.
# They are used especially for higher-order functions, where functions are passed as arguments to other functions.

sum = lambda a,b: a+b
print(sum(3,4))  # Output: 7


average  = lambda a,b: (a+b)/2
print(average(3,4))  # Output: 3.5