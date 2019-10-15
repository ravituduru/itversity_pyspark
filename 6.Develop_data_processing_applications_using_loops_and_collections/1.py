def readData(datapath):
    datafile=open(datapath)
    datastr=datafile.read()
    datalist=datastr.splitlines()
    return datalist

#columns in order_items
#id,order_id,product_id,quantity,sub-total,price
orderItems=readData("D:\\Ravi\\data-master\\retail_db\\order_items\\part-00000")
#1.Create a Function to get revenue for a given order_id(from order_items)
def getOrdeRevenue(orderItems,orderid):
    orderevenue=0.0
    for orderItem in orderItems:
        if int(orderItem.split(",")[1])==orderid:
            orderevenue+=float(orderItem.split(",")[4])
    return orderevenue
print(getOrdeRevenue(orderItems,2))

#2.Create a function to get revenue for each order_id
def getOrdePerRevenue(orderItems):
    ordeperrevenue={}
    for orderItem in orderItems:
        ordertuple=(int(orderItem.split(",")[1]),float(orderItem.split(",")[4]))
        if ordeperrevenue.get(ordertuple[0]):
            ordeperrevenue[ordertuple[0]]+=ordertuple[1]
        else:
            ordeperrevenue[ordertuple[0]]=ordertuple[1]
    return ordeperrevenue

print(getOrdePerRevenue(orderItems))
# orderItems1='1,1,957,1,299.98,299.98'
#
# revenue={}
# a=(int(orderItems1.split(",")[1]),float(orderItems1.split(",")[4]))
# #print(a)
# if(revenue.get(int(orderItems1.split(",")[1]))):
#     revenue[a[0]]=revenue[a[0]]+a[1]
# else:
#     revenue[int(orderItems1.split(",")[1])]=float(orderItems1.split(",")[4])
#
# orderItems2='2,2,1073,1,199.99,199.99'
# a=(int(orderItems2.split(",")[1]),float(orderItems2.split(",")[4]))
# #print(a)
#
# if(revenue.get(int(orderItems2.split(",")[1]))):
#     revenue[a[0]]=revenue[a[0]]+a[1]
# else:
#     revenue[int(orderItems2.split(",")[1])]=float(orderItems2.split(",")[4])
#
# #print(revenue)
# orderItems3='3,2,502,5,250.0,50.0'
# a=(int(orderItems3.split(",")[1]),float(orderItems3.split(",")[4]))
#
# if(revenue.get(int(orderItems3.split(",")[1]))):
#     print(revenue)
#     print(revenue[a[0]])
#     revenue[a[0]]=revenue[a[0]]+a[1]
# else:
#     revenue[int(orderItems3.split(",")[1])]=float(orderItems3.split(",")[4])
#
# print(revenue)

#3.create a function to get daily revenue using orders which are completed or closed and order items
