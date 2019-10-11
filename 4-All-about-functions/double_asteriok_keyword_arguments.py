#variable length arguments
# *numbers defines you can pass mutiple  numbers
# **keywords to pass arguments in key value pairs
def total(initial=5,*numbers,**keywords):
    count=initial
    for num in numbers:
        count+=num
    for key in keywords:
        count+=keywords[key]
    return count


print(total(10,1,2,3,vegetables=50,fruits=100))