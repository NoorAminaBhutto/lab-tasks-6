nums=[2,3,2,5,3,2,5,8]
result={}
for n in nums:
    if n in result:
        result[n]=result[n]+1
    else:
        result[n]=1
print(result)