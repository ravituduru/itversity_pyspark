#sum of the integers using the lambda
def total(lb,ub,f):
    count=0
    for i in range(lb,ub+1):
        count+=f(i)
    return count


print(total(5,10,lambda i:i))

