def SumofIntergers(lb,ub):
    l=lb-1
    return (ub*(ub+1))/2 - (l*(l+1))/2

print(SumofIntergers(5,10))