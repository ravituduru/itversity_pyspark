l=list(range(1,20))

leven=filter(lambda f : True if (f%2==0) else False,l)
#or both are same
leven=filter(lambda f:f%2==0,l)

for i in leven:
    print(i)