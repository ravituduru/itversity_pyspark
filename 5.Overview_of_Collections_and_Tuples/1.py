ordersPath="/home/ravi-pc/data-master/retail_db/orders/part-00000"
#orderFile=open(ordersPath)
#ordersData=orderFile.read()
#print(ordersData)
#ordersDatainline=ordersData.splitlines()
#print(len(ordersDatainline))
#print(ordersDatainline)
#print(ordersDatainline[:10])
#print(type(ordersDatainline))

def readData(path):
    dataFile=open(path)
    datastr=dataFile.read()
    datalist=datastr.splitlines()
    return datalist

print(readData("/home/ravi-pc/data-master/retail_db/order_items/part-00000"))

