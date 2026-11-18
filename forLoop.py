# string = "hello"


# # membership operator 

# for var in string:
#     print(var)

# # in => we can use in ooperstor to check if a value is present in a sequence or not. It returns True if the value is found in the sequence, otherwise it returns False.    

# if 'o' in string:
#     print("o is present in the string")

# for i in range(5):
#     print(i)

# word = "artificial intelligence"

# # count the number of occurrences of 'i' in the word => 5

# count = 0

# for ch in word:
#     if ch == 'i':
#         count +=1

# print ("The number of occurrences of 'i' in the word is:", count)        


#  count vowels in a string

word = "artificial"
count = 0
for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1

print("The number of vowels in the word is:", count)