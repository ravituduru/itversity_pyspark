l=list(range(1,20))

leven=filter(lambda f : True if (f%2==0) else False,l)

for i in leven:
    print(i)