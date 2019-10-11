#variable length arguments
# *numbers defines you can pass mutiple  numbers
def total(initial=5,*numbers):
    count=initial
    for num in numbers:
        count+=num
    return count


print(total(10,1,2,3,4))