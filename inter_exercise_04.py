#https://www.w3schools.com/python/python_try_except.asp
# did not know python exceptions worked but found explanation and saw tried till value error worked

nums = list()
while len(nums) < 5:
    print(len(nums)+1 ,": ", end=' ')
    try:
        num = int(input("Please enter an integer:" ))
        nums.append(num)
    except ValueError:
        print("Invalid Input. Please enter an int")

sum = 0

for ints in nums:
    sum = sum + ints

print("You sum is: ", sum)