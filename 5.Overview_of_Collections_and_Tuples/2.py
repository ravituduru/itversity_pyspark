def readData(path):
    filepath=open(path)
    strdata=filepath.read()
    data=strdata.splitlines()
    return data

orders=readData("D:\\Ravi\\data-master\\retail_db\\orders\\part-00000")

1.#sort the data according to the customerid
sortedatabyid=sorted(orders,key=lambda k:int(k.split(",")[2]))
print(sortedatabyid[:2])

2.#get all orders status from the order data
orderstatus=[]
for order in orders:
    status=order.split(",")[3]
    orderstatus.append(status)
#print(orderstatus)
#print(set(orderstatus))
#or
orderstatus1=set([])

for order in orders:
    orderstatus1.add(order.split(",")[3])

print(orderstatus1)