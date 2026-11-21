def average(a,b,c):
    avg=a+b+c/3
    return avg


print(average(3,4,5))    



# Default parameter

def sum(a,b=5):
    s=a+b
    return s

print(sum(3))  # Output: 8
print(sum(3,4))  # Output: 7